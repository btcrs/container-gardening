from Adafruit_BME280 import *
sensor = BME280(mode=BME280_OSAMPLE_8)
import schedule

def report_temperature():
    temperature = sensor.read_temperature()
    data = {'parameter': 'temperature', 'value': str(temperature)}

def report_pressure():
    pascals = sensor.read_pressure()
    pressure = pascals / 100
    data = {'parameter': 'pressure', 'value': str(pressure)}

def report_humidity():
    humidity = sensor.read_humidity()
    data = {'parameter': 'humidity', 'value': str(humidity)}

def get_data():
    report_temperature()
    report_pressure()
    report_humidity()

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
