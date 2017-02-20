from aosong import am2315
sensor = am2315.Sensor()

def get_data():
    temperature = sensor.temperature(True)
    humidity = sensor.humidity()
    data = str(temperature) + ", " + str(humidity)
    print(data)

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)

