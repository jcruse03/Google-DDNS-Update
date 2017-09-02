#!/usr/bin/env python3
import base64
import json
import socket
import time
import urllib.parse
import urllib.request

# ------User Config------

# Update interval in seconds
# Recommended 60 or greater to allow dns servers time to update
TICKTIME = 120

# Your google DDNS credentials
# Go to domains.google.com, configure dns, then under Sythetic records find Dynamic DNS.
# Click the drop down and click view credentials.
GOOGLE_DDNS_USER = ''
GOOGLE_DDNS_PASS = ''

# subdomain.domain.com
MY_DOMAIN = ''

# ------End User Config------

DEBUG = False

def send_request(ip_addr):
	"""Sends a post request to https://domains.google.com and updates the DDNS ip address.
	Prints the response if DEBUG is set to True.
	
	Keyword arguments:
	ip -- the ip address to update
	"""
	url = 'https://domains.google.com/nic/update?'
	values = {'hostname' : MY_DOMAIN,
    	      'myip' : ip_addr}

	data = urllib.parse.urlencode(values).encode("utf-8")
	req = urllib.request.Request(url, data)
	base64_user_pass = base64.encodestring(('%s:%s' % (GOOGLE_DDNS_USER, GOOGLE_DDNS_PASS)).encode()).decode().replace('\n', '')
	req.add_header('Authorization', 'Basic %s' % base64_user_pass)
	response = urllib.request.urlopen(req)
	page = response.read()
	if DEBUG:
		print(page)

def get_my_ip():
	"""Returns the current public ip address"""
	info = json.loads(urllib.request.urlopen("https://api.ipify.org?format=json").read())
	return info['ip']

def get_domain_ip(domain):
	"""Returns the current ip address of domain
	
	Keyword arguments:
	domain -- return this domains' ip address
	"""
	return socket.gethostbyname(domain)

if DEBUG:
	send_request('162.11.2.1')

while True:
	time.sleep(TICKTIME - time.time() % TICKTIME)
	if get_domain_ip(MY_DOMAIN) != get_my_ip():
		if DEBUG:
			print(get_my_ip())
			print(get_domain_ip(MY_DOMAIN))
		send_request(get_my_ip())
