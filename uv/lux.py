import time
import Adafruit_TCS34725
import smbus

tcs = Adafruit_TCS34725.TCS34725()
tcs.set_interrupt(False)
#tcs = Adafruit_TCS34725.TCS34725(address=0x30, busnum=2)

r, g, b, c = tcs.get_raw_data()
color_temp = Adafruit_TCS34725.calculate_color_temperature(r, g, b)
lux = Adafruit_TCS34725.calculate_lux(r, g, b)

print('Color: red={0} green={1} blue={2} clear={3}'.format(r, g, b, c))

if color_temp is None:
    print('Too dark to determine color temperature!')
else:
    print('Color Temperature: {0} K'.format(color_temp))

print('Luminosity: {0} lux'.format(lux))

tcs.set_interrupt(True)
tcs.disable()
