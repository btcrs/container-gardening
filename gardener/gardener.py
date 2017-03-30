from flask import Flask, request
from flask_restful import Resource, Api
from tinydb import TinyDB, Query
from json import dumps, loads
from pprint import pprint
import requests
import os

db = TinyDB('tiny.json')
url = (os.environ['API'] + '/dev/datum')
headers = {'x-api-key': os.environ['KEY'],'Content-Type': 'application/json'}

app = Flask(__name__)
api = Api(app)

class data(Resource):
    def post(self):
        db.insert(request.json)
        if len(db.all()) >= 20:
            pprint(db.all())
            db.purge()
        try:
           sent_request = self.send_data(request.json)
        except:
            print(sent_request)
        return request.json 

    def get(self):
        return db.all()

def send_data(self, entry):
    request = requests.post(url, headers=headers, json=entry)
    print(request)

api.add_resource(data, '/dev/datum')

if __name__ == '__main__':
     app.run(host='0.0.0.0')


