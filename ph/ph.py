#!/usr/bin/env python
import time
import schedule
import sys
sys.path.insert(0, '../reporter')
from reporter import reporter
from active import ph

reporter = reporter()
ph = ph.Ph()

def get_data():
    pH = ph.poll()
    print(pH)
    reporter.send_data("ph", pH)

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
