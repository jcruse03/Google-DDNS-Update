#!/usr/bin/env python3
import base64
import logging
import os
import socket
import time
import urllib.error
import urllib.parse
import urllib.request

DEBUG = False

logging.basicConfig(format='%(asctime)s %(message)s'
                    , filename='/var/log/ddns-update.log', level=logging.DEBUG)
logging.info('Started')

class Record:
    """Holds and updates subdomain records on domains.google.com"""
    def __init__(self, sub_domain, user, password):
        self.sub_domain = sub_domain
        self.user = user
        self.password = password

    def show(self):
        """print the record"""
        print(self.sub_domain + ' ' + self.user + ' ' + self.password)

    def get_ip(self):
        """Returns the current ip address of self.sub_domain"""
        return socket.gethostbyname(self.sub_domain)

    def update_ip(self, ip_addr):
        """Sends a post request to https://domains.google.com and updates the DDNS ip address.
        Prints the response if DEBUG is set to True.
        Keyword arguments:
        ip -- the ip address to update
        """
        url = 'https://domains.google.com/nic/update?'
        values = {'hostname' : self.sub_domain,
                  'myip' : ip_addr}

        data = urllib.parse.urlencode(values).encode("utf-8")
        req = urllib.request.Request(url, data)
        base64_user_pass = base64.encodestring(
            ('%s:%s' % (self.user, self.password)).encode()).decode().replace('\n', '')
        req.add_header('Authorization', 'Basic %s' % base64_user_pass)
        response = urllib.request.urlopen(req)
        page = response.read()
        logging.info(page)
        if DEBUG:
            print(page)

class Domain:
    def __init__(self):
        self.records = []
        self.tick_time = 120

    def add(self, sub_domain, user, password):
        """Append a record to self.records"""
        self.records.append(Record(sub_domain, user, password))

    def show(self):
        """Print records"""
        for rec in self.records:
            rec.show()

def get_my_ip():
    """Returns the current public ip address"""
    info = str(urllib.request.urlopen(
        "https://api.ipify.org?format=txt").read()).replace('b', '').replace("'", '')
    return info

def read_conf():
    """Reads file "/etc/ddns-update.conf and returns a Domain object"""
    domain = Domain()
    try:
        file = open('/etc/ddns-update.conf')
        counter = 1
        for line in file:
            temp = line.split()
            if line[0] == '#' or line.isspace():
                continue
            elif str(temp[0]) == 'TICKTIME':
                try:
                    domain.tick_time = int(temp[1])
                except ValueError:
                    logging.warning(
                        'TICKTIME must be an integer ie: <TICKTIME int> in ' +
                        '/etc/ddns-update.conf, reverting to default')
            elif len(temp) == 3:
                if DEBUG:
                    print(temp)
                domain.add(str(temp[0]), str(temp[1]), str(temp[2]))
            else:
                logging.warning('invalid entry on line ' + str(counter) +
                                ' in /etc/ddns-update.conf. Must be 3 arguments: ' +
                                'subdomain user password, or TICKTIME NUM ')
                if DEBUG:
                    print('invalid entry on line ' + str(counter) +
                          ' in /etc/ddns-update.conf. Must be 3 arguments: ' +
                          ' subdomain user password, or TICKTIME NUM ')
            counter += 1
        file.close()
    except OSError:
        logging.error('cannot open /etc/ddns-update.conf exiting')
        exit(1)
    if len(domain.records) < 1:
        logging.error('No records found in /etc/ddbs-update.conf, exiting.')
        exit(1)
    return domain

DOMAINS = read_conf()
if DEBUG:
    DOMAINS.tick_time = 10
    logging.info('tick_time = ' + str(DOMAINS.tick_time))

COUNT = 0

while True:
    for record in DOMAINS.records:
        try:
            current_ip = get_my_ip()
            dns_ip = record.get_ip()
            if DEBUG and COUNT < len(DOMAINS.records):
                record.update_ip(socket.gethostbyname('google.com'))
                COUNT += 1
            if current_ip != dns_ip:
                logging.info('Updating: ' + record.sub_domain +
                             ' from: ' + dns_ip + ' to: ' + current_ip)
                if DEBUG:
                    print('updating ' + record.get_ip() + ' to ' + get_my_ip())
                record.update_ip(current_ip)
            else:
                logging.info('no change on ' + record.sub_domain +
                             ' dns_ip = ' + dns_ip + ', current_ip= ' + current_ip)
        except urllib.error.URLError:
            logging.error('URLError: connection may be down')
    time.sleep(DOMAINS.tick_time - time.time() % DOMAINS.tick_time)
    #truncate log file when it gets too large
    if os.stat('/var/log/ddns-update.log').st_size > 10485760:
        with open('/var/log/ddns-update.log', 'w'):
            logging.info('cleared /var/log/ddns-update.log')
