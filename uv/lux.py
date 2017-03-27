import time
import schedule
import Adafruit_TCS34725
import smbus

import sys
sys.path.insert(0, '../reporter')
from reporter import reporter

reporter = reporter()
tcs = Adafruit_TCS34725.TCS34725()

def get_color(r, g, b, c):
    reporter.send_data("color", 'red={0} green={1} blue={2} clear={3}'.format(r, g, b, c))

def get_temperature(r, g, b):
    temperature = Adafruit_TCS34725.calculate_color_temperature(r, g, b)
    reporter.send_data("Color Temperature", temperature)

def get_luminosity(r, g, b):
    lux = Adafruit_TCS34725.calculate_lux(r, g, b)
    reporter.send_data("Luminosity", lux)

def get_data():
    tcs.enable()
    tcs.set_interrupt(False)

    r, g, b, c = tcs.get_raw_data()
    get_color(r, g, b, c)
    get_temperature(r, g, b)
    get_luminosity(r, g, b)
    
    tcs.set_interrupt(True)
    tcs.disable()

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)



