import w1thermsensor 
import schedule
import time

def job():
    for sensor in w1thermsensor.W1ThermSensor.get_available_sensors():
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
