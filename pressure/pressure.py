#!/usr/bin/env python
import time
from envirophat import weather, leds


try:
    while True:
        pressure = weather.pressure()
        print("{}".format(pressure))
        time.sleep(0.1)
