import w1thermsensor 
import schedule
import requests
import json
import time
import os

def job():
    for sensor in w1thermsensor.W1ThermSensor.get_available_sensors():
        send_data(sensor.get_temperature())

def send_data(temperature):
    entry = json.dumps({'parameter': 'temperature', 'value': str(temperature)})
    url = (os.environ['API'] + '/dev/datum')
    requests.post(url, data=entry)

schedule.every(15).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
