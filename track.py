import os
import io
import subprocess
import yaml
import json
import requests

with io.open('config.yml', 'r') as stream:
	try:
		CONFIG_VARS = yaml.safe_load(stream)
	except yaml.YAMLError as err:
		print(err)
		raise

MASTER_URL = CONFIG_VARS['MASTER']['URL']
MASTER_ENDPOINTS = CONFIG_VARS['MASTER']['ENDPOINTS']

def login(log):
	l = log.split()
	print("LOGIN")

	payload = {
		"month": l[0],
		"date": l[1],
		"time": l[2],
		"host": l[3],
		"user": l[8],
		"ip": l[10],
		"port": l[12]
	}

	# payload = json.dumps(payload)
	url = MASTER_URL + MASTER_ENDPOINTS['LOGIN']

	f = requests.post(url, json=payload)


def logout(log):
	l = log.split()
	print("LOGOUT")

	payload = {
		"month": l[0],
		"date": l[1],
		"time": l[2],
		"host": l[3],
		"user": l[8],
		"ip": l[9],
		"port": l[11]
	}

	# payload = json.dumps(payload)
	url = MASTER_URL + MASTER_ENDPOINTS['LOGOUT']

	f = requests.post(url, json=payload)

def track():
	
	auth_log = CONFIG_VARS['AUTH_LOG']

	f = subprocess.Popen(['tail', '-F', auth_log], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	
	while True:
		line = f.stdout.readline().decode()
		if "sshd" in line:
			if "Accepted" in line:
				login(line)
			elif "Disconnected" in line:
				logout(line)

track()
