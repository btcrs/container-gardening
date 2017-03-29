import quick2wire.i2c as i2c
import time
import array
import math

class Sensor:

    def __init__(self, address=0x5C, debug=False):
        self.channel = 1
        self.address = address  
        self.bus = i2c.I2CMaster() 		
        self.lastError = None   	
        self.debug = debug       


    def data(self):
        data = None

        try:
            self.bus.transaction(i2c.writing(self.address, bytes([0x03,0x0,0x04])))
        except:
             pass
        time.sleep(0.125)

        try:
            self.bus.transaction(i2c.writing(self.address, bytes([0x03,0x0,0x04])))
            data = self.bus.transaction(i2c.reading(self.address, 0x08))
            data = bytearray(data[0])
        except IOError as e:
            self.lastError = 'I/O Error({0}): {1}'.format(e.errno,e.strerror)
            return None

        if data[0] != 0x03 and data[1] != 0x04:
            self.lastError('Error reading data from AM2315 device.')
            return None

        cmd_code = data[0]
        byte_cnt = data[1]
        humid_H  = data[2]
        humid_L  = data[3]
        temp_H   = data[4]
        temp_L   = data[5]
        crc_H    = data[6]
        crc_L    = data[7]

        negative = False
        humidity = (humid_H*256+humid_L)/10

        if temp_H&0x08:
           negative = True
        temp_H &=0x7F

        tempC = (temp_H*256+temp_L)/10
        tempF = self.c_to_f(tempC)

        crc = 256*data[7] + data[6]
        t = bytearray([data[0], data[1], data[2], data[3], data[4], data[5]])
        c = self.verify_crc(t)

        if crc != c:
            assert(0)
            self.lastError('CRC error in sensor data.')
            return None

        if negative:
            tempC = -abs(tempC)
            tempF = -abs(tempF)

        return (humidity, tempC, tempF)


    def humidity(self):
        humidity = None
        if self.data():
            time.sleep(.25)
            humidity = self.data()[0]
        return humidity

    def temperature(self, fahrenheit=False):
        time.sleep(.25)
        if self.data():
           return self.data()[2] if fahrenheit else self.data()[1]
        else:
            return None

    def fahrenheit(self):
        return self.temperature(True)

    def celsius(self):
        return self.temperature()

    def verify_crc(self, char):
        crc = 0xFFFF
        for l in char:
            crc = crc ^ l
            for i in range(1,9):
                if(crc & 0x01):
                    crc = crc >> 1
                    crc = crc ^ 0xA001
                else:
                    crc = crc >> 1
        return crc


    def c_to_f(self, celsius):
        if celsius == 0:
            return 32
        else:
            try:
                tempF = float((celsius*9/5)+32)
                return (math.trunc(tempF*10))/10
            except:
                self.lastError = 'Error converting %s celsius to fahrenheit' % celsius
                return None

    def last_error(self):
        return self.lastError
