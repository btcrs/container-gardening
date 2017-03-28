import w1thermsensor 
import schedule
import time
import sys
sys.path.insert(0, '../../reporter')
from reporter import reporter

reporter = reporter()

def job():
    sensors = w1thermsensor.W1ThermSensor.get_available_sensors()
    if len(sensors) < 1:
        print "W1 Offline..."
    else:
        for sensor in sensors :
            reporter.send_data("temperature", sensor.get_temperature())

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
