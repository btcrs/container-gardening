import w1thermsensor 
import schedule
import requests
import json
import time
import os

def job():
    for sensor in w1thermsensor.W1ThermSensor.get_available_sensors():
        temperature = sensor.get_temperature()
        print("Sensor %s has temperature %.2f" % (sensor.id, temperature))
        send_data(temperature)

def send_data(temperature):
    entry = json.dumps({'parameter': 'temperature', 'value': str(temperature)})
    url = (os.environ['API'] + '/dev/datum')
    print(url)
    r = requests.post(url, data=entry)
    print(r.status_code)

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
