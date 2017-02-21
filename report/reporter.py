import json
import os

class reporter:

    def __init__(self):
        self.url = (os.environ['API'] + '/dev/datum')

    def send_data(self, parameter, value):
        entry = json.dumps({'parameter': str(parameter), 'value': str(value)})
        requests.post(self.url, data=entry)

