# Heimdall - Serverside

This repository contains code for the server-side application of Heimdall SSH Logging system.

---

### Setup Instructions

- Clone this repository.
- Initialize a virtual environment and install all the necessary packages using ```requirements.txt```
	```pip install -r requirements.txt```

- Set environment variables for flask
	```
	export FLASK_APP=server
	export FLASK_ENV=development
	```

- You can change the FLASK_ENV according to your needs.
- Copy ```config-stencil.yml``` to ```config.yml```.

- Now, set the environment variable in ```config.yml``` as follows:
	```
	destination_file: path/to/the/authorized_keys/file/in/the/.ssh/directory/
	```

- Run ```flask run``` in the directory containing ```server.py```

---

### Heimdall-ssh-keys repository setup instructions

- Add an entry in the ```server-mappings.yml``` file for this server.
- Make a file in the ```servers/``` directory with the same name as in ```server-mappings.yml```

### Working

If someone wants access to your ssh server, all he/she has to do is make a PR on "Heimdall-ssh-keys" after uploading his/her Public Key in the "public-keys" folder and entering the name of the file containing the Public Key to that corresponding server's file in the ```servers/``` directory.

---

#### Happy Hacking
