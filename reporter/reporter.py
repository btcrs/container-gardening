import requests
import json
import os

class reporter:

    def __init__(self):
        self.url = (os.environ['GARDENER'] + '/dev/datum')

    def send_data(self, parameter, value):
        entry = {'parameter': str(parameter), 'value': str(value)}
        try:
            requests.post(self.url, json=entry)
        except requests.exceptions.RequestException as e:
            print(e)
