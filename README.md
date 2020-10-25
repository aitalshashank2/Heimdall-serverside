# Heimdall - Serverside

This repository contains code for the server-side applications of Heimdall SSH Logging system.

---
## Heimdall

Heimdall is a GitHub based server login manager. It uses GitHub to track the SSH Keys and manage the access of the servers.

For more information, please head to [Heimdall](https://github.com/aitalshashank2/Heimdall-Master)

---

## Setup Instructions

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

- Detach this terminal session and open a new terminal

- Run `python track.py` to start listening to the auth logs

- Serverside is up and running now.
