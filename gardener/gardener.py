from flask import Flask, request
from flask_restful import Resource, Api
from tinydb import TinyDB, Query
from json import dumps, loads
from pprint import pprint
import os

db = TinyDB('tiny.json')
#url = (os.environ['API'] + '/dev/datum')

app = Flask(__name__)
api = Api(app)

class data(Resource):
    def post(self):
        db.insert(request.json)
        if len(db.all()) >= 20:
            pprint(db.all())
            db.purge()
        #requests.post(self.url, data=entry)
        return request.json 

    def get(self):
        return db.all()

api.add_resource(data, '/dev/datum')

if __name__ == '__main__':
     app.run(host='0.0.0.0')
