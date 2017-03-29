#!/usr/bin/env python
import time
import schedule
import sys
sys.path.insert(0, '../reporter')
from reporter import reporter
from ph import Ph

reporter = reporter()
ph = Ph()

def get_data():
    try:
        pH = ph.poll()
        reporter.send_data("ph", pH)
    except:
        print "pH Offline..."

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
