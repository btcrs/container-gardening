from aosong import am2315
import schedule
import time
sensor = am2315.Sensor()
import sys
sys.path.insert(0, '../reporter')

from reporter import reporter

def report_temperature():
    temperature = sensor.temperature(True)
    reporter.send_data("temperature", temperature)

def report_humidity():
    humidity = sensor.humidity()
    reporter.send_data("humidity", humidity)

def get_data():
    report_temperature()
    report_humidity()

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
