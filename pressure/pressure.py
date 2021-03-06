#!/usr/bin/env python
import time
import schedule

import sys
sys.path.insert(0, '../reporter')

from reporter import reporter
from envirophat import weather, leds

reporter = reporter()

def get_data():
    pressure = weather.pressure()
    reporter.send_data("pressure", '{0:0.3f}'.format(pressure))

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
