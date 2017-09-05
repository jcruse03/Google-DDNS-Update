#!/usr/bin/env python3
import base64
import json
import logging
import socket
import time
import urllib.parse
import urllib.request

#clear the log file
with open('/var/log/ddns-update.log', 'w'):
    pass

DEBUG = False

logging.basicConfig(format='%(asctime)s %(message)s', filename='/var/log/ddns-update.log', level=logging.DEBUG)
logging.info('Starting')

class Record:
    def __init__(self, sub_domain, user, password):
		self.sub_domain = sub_domain
		self.user = user
		self.password = password

	def show(self):
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
		base64_user_pass = base64.encodestring(('%s:%s' % (self.user, self.password)).encode()).decode().replace('\n', '')
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
		self.records.append(Record(sub_domain, user, password))

	def show(self):
		for rec in self.records:
			rec.show()
		

def get_my_ip():
	"""Returns the current public ip address"""
	info = json.loads(urllib.request.urlopen("https://api.ipify.org?format=json").read())
	return info['ip']

def read_conf():
	# reads file "/etc/ddns-update.conf", inits domains
	domain = Domain()
	f = open('/etc/ddns-update.conf')
	count = 1
	for line in f:
		temp = line.split()
		if (line[0] == '#' or line.isspace()):
			continue
		elif (str(temp[0]) == 'TICKTIME'):
			domain.tick_time = int(temp[1])
		elif (len(temp) == 3):
			if DEBUG:
				print(temp)
			domain.add( str(temp[0]), str(temp[1]), str(temp[2]) )
		else:
			logging.warning('invalid entry on line ' + str(count) + ' in /etc/ddns-update.conf. Must be 3 arguments: subdomain user password, or TICKTIME NUM ')
			if DEBUG:
				print ('invalid entry on line ' + str(count) + ' in /etc/ddns-update.conf. Must be 3 arguments: subdomain user password, or TICKTIME NUM ')
		count += 1

	f.close()
	if (len(domain.records) < 1):
		logging.error('No records found in /etc/ddbs-update.conf, exiting.')
		exit()
	return domain


domains = read_conf()
print(domains.tick_time)

count = 0

while True:
	time.sleep(domains.tick_time - time.time() % domains.tick_time)

	for record in domains.records:
		if DEBUG and count < len(domains.records):
			record.update_ip(socket.gethostbyname('google.com'))
			count += 1
		if record.get_ip() != get_my_ip():
			logging.info('Updating: ' + record.sub_domain + ' from: ' + record.get_ip() + ' to: ' + get_my_ip())
			if DEBUG:
				print('updating ' + record.get_ip() + ' to ' + get_my_ip())
			record.update_ip(get_my_ip())
