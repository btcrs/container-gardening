import time
import random
import RPi.GPIO as GPIO

class flow_sensor():

    milliseconds = 1000.0

    def __init__(self):
        self.clicks = 0
        self.last_click = int(time.time() * flow_sensor.milliseconds)
        self.click_delta = 0
        self.hertz = 0.0
        self.flow = 0.0

    def update(self, current_time):
        self.clicks += 1
        self.click_delta = max((current_time - self.last_click), 1)
        if (self.click_delta < 1000):
	        self.hertz = flow_sensor.milliseconds / self.click_delta
	        self.flow = self.hertz / (60 * 7.5)  # Liters/S
        self.last_click = current_time

    def get_flow(self):
         return str(round(self.flow, 3)) + ' L/s'

fm = flow_sensor()

def click(channel):
    current_time = int(time.time() * flow_sensor.milliseconds)
    fm.update(current_time)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(21, GPIO.RISING, callback=click, bouncetime=20)
    while True:
        pass
