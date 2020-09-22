from flask import Flask, request
import io
import yaml
import json

with io.open('config.yml', 'r') as stream:
    data_loaded = yaml.safe_load(stream)

destination_file = data_loaded["destination_file"]

app = Flask(__name__)

@app.route('/', methods=['POST'])

def server():
    payload = request.get_json()
    authorized_keys = json.loads(payload)["authorized_keys"]

    f = open(destination_file, 'w')
    f.write(authorized_keys)

    return "OK"
