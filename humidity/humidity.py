import am2315
import schedule
import time
import sys
sys.path.insert(0, '../reporter')
from reporter import reporter

sensor = am2315.Sensor()
reporter= reporter()

def report_temperature():
    try:
        temperature = sensor.temperature(True)
        if temperature:
            reporter.send_data("temperature", temperature)
    except:
        pass
     

def report_humidity():
    try:
        humidity = sensor.humidity()
        if humidity:
            reporter.send_data("humidity", humidity)
    except:
        pass

def get_data():
    report_temperature()
    report_humidity()

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
