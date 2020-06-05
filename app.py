import json
from flask import Flask
APP = Flask(__name__)

@APP.route('/')
def main():
    message = {'message':'Hello to the nClouds'}
    return json.dumps(message)

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5020)
