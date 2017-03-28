import serial

class Ph():

    def __init__(self):
        self.usbport = '/dev/ttyAMA0'
        self.serial = serial.Serial(self.usbport, 9600, timeout=3)

    def read_ph(self):
        try:
            line = ""
            while True:
                data = self.serial.read()
                if data == "\r":
                    return line
                else:
                    line = line + data

        except serial.SerialException as e:
            return None

    def poll(self):
        self.serial.write("R\r")
        ph = self.read_ph()
        if ph is not None:
            print "Ph: ", ph
        return ph

    def update_record(self):
        '''
        Send a message to the api
        '''
        pass
