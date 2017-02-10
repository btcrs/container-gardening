import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')
device_file = device_folder[0] + '/w1_slave' if len(device_folder) > 0 else None
 
def read_temperature():
    lines = None
    if device_file:
        device = open(device_file, 'r')
        lines = device.readlines()
        device.close()
    return lines
 
def report_temperature():
    lines = read_temperature()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    reading = lines[1].find('t=')
    if reading != -1:
        temperature_string = lines[1][reading+2:]
        celcius = float(temperature_string) / 1000.0
        fahrenheit = str(celcius * 9.0 / 5.0 + 32.0)
        return "The current temperature is: " + fahrenheit + "*F/" + str(celcius) + "*C"
	
while True:
	print(report_temperature())	
	time.sleep(1)
