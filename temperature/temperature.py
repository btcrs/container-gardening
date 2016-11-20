#!/usr/bin/env python
import time
from envirophat import weather, leds


try:
    while True:
        temperature = weather.temperature()
        print("{} degrees celcius".format(temperature))
        time.sleep(0.1)
