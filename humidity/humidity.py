from aosong import am2315
import schedule
sensor = am2315.Sensor()

def report_temperature():
    temperature = sensor.temperature(True)
    data = {'parameter': 'temperature', 'value': str(temperature)}

def report_humidity():
    humidity = sensor.humidity()
    data = {'parameter': 'humidity', 'value': str(humidity)}

def get_data():
    report_temperature()
    report_humidity()

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
