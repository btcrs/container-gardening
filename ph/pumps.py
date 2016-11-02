from rrb3 import *
import time

class Pumps():
    def __init__(self, lower, upper):
        self.lower_bound = lower
        self.upper_bound = upper
        self.controller = RRB3(12, 12)

    def regulate(self, ph):
        if ph < self.lower_bound:
            self.dispense_alkali()
        elif ph > self.upper_bound:
            self.dispense_acid()
        else:
            print "Good Ph!"

    def dispense_acid(self):
	    self.controller.set_motors(0, 0, 1, 0)
    	time.sleep(1)
    	self.controller.stop()

    def dispense_alkali(self):
	    self.controller.set_motors(1, 0, 0, 0)
    	time.sleep(1)
    	self.controller.stop()
