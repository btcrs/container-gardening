import serial
import time

print("Calibration will begin with ph solution 4, followed by 7 and 10")

usbport = '/dev/ttyAMA0'
ser = serial.Serial(usbport, 9600, timeout=3)

raw_input("Press Enter to calibrate low...")
ser.write("cal,low,4\r")
raw_input("Press Enter to calibrate med...")
ser.write("cal,mid,7\r")
raw_input("Press Enter to calibrate high...")
ser.write("cal,high,10\r")
