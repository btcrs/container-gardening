from Adafruit_BME280 import *
import schedule
import sys
sys.path.insert(0, '../reporter')

from reporter import reporter
reporter = reporter()

sensor = BME280(mode=BME280_OSAMPLE_8)

def report_temperature():
    temperature = sensor.read_temperature()
    reporter.send_data("temperature", '{0:0.3f}'.format(temperature))

def report_pressure():
    pascals = sensor.read_pressure()
    pressure = pascals / 100
    reporter.send_data("pressure", '{0:0.3f}'.format(pressure))

def report_humidity():
    humidity = sensor.read_humidity()
    reporter.send_data("humidity", '{0:0.3f}'.format(humidity))

def get_data():
    try:
        report_temperature()
        report_pressure()
        report_humidity()
    except:
        print "BME280 Offline..."

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
