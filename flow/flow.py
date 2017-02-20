import time
import random
import RPi.GPIO as GPIO

class FlowMeter():
    MS_IN_A_SECOND = 1000.0
    clicks = 0
    lastClick = 0
    clickDelta = 0
    hertz = 0.0
    flow = 0 # liters/second

    def __init__(self):
        self.clicks = 0
        self.lastClick = int(time.time() * FlowMeter.MS_IN_A_SECOND)
        self.clickDelta = 0
        self.hertz = 0.0
        self.flow = 0.0

    def update(self, currentTime):
        self.clicks += 1
        self.clickDelta = max((currentTime - self.lastClick), 1)
        if (self.clickDelta < 1000):
	      self.hertz = FlowMeter.MS_IN_A_SECOND / self.clickDelta
	      self.flow = self.hertz / (60 * 7.5)  # In Liters per second
        self.lastClick = currentTime
        print(self.getFlow())

    def getClickDelta(self):
         return str(self.clickDelta) + ' ms'
  
    def getHertz(self):
         return str(round(self.hertz,3)) + ' Hz'
  
    def getFlow(self):
         return str(round(self.flow,3)) + ' L/s'

fm = FlowMeter()

def doAClick(channel):
    currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
    fm.update(currentTime) 

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(21, GPIO.RISING, callback=doAClick, bouncetime=20)
    while True:
        pass
