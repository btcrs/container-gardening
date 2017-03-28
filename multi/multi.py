from Adafruit_BME280 import *
sensor = BME280(mode=BME280_OSAMPLE_8)
import schedule

import sys
sys.path.insert(0, '../reporter')

from reporter import reporter

def report_temperature():
    temperature = sensor.read_temperature()
    reporter.send_data("temperature", temperature)

def report_pressure():
    pascals = sensor.read_pressure()
    pressure = pascals / 100
    reporter.send_data("pressure", pressure)

def report_humidity():
    humidity = sensor.read_humidity()
    reporter.send_data("humidity", humidity)

def get_data():
    report_temperature()
    report_pressure()
    report_humidity()

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
