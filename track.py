import os
import io
import subprocess
import yaml

def login(log):
	l = log.split()
	print("LOGIN")
	month = l[0]
	date = l[1]
	time = l[2]
	device = l[3]
	user = l[8]
	ip = l[10]
	port = l[12]

	print(month, date, time, device, user, ip, port)

def logout(log):
	l = log.split()
	print("LOGOUT")
	month = l[0]
	date = l[1]
	time = l[2]
	device = l[3]
	user = l[8]
	ip = l[9]
	port = l[11]

	print(month, date, time, device, user, ip, port)

def track():
	with io.open('config.yml', 'r') as stream:
		try:
			CONFIG_VARS = yaml.safe_load(stream)
		except yaml.YAMLError as err:
			print(err)
			raise FileNotFoundError
	
	auth_log = CONFIG_VARS['auth_log']

	f = subprocess.Popen(['tail', '-F', auth_log], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
	
	while True:
		line = f.stdout.readline().decode()
		if "sshd" in line:
			if "Accepted" in line:
				login(line)
			elif "Disconnected" in line:
				logout(line)

track()
