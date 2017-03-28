import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import schedule
import time
import sys
sys.path.insert(0, '../reporter')

from reporter import reporter

class depth_sensor:

    def __init__(self, port, device):
        self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(port, device))
        self.dry = 912.0
        self.inch = 5.0

    def get_depth(self):
        reading = self.get_raw_adc()
        depth = (reading-self.dry)/self.inch
        return depth if depth > 0.0 else 0

    def get_raw_adc(self):
        return float(self.mcp.read_adc(0))

sensor = depth_sensor(0, 0)
def get_data():
    inches = sensor.get_depth()
    reporter.send_data("depth", depth)

schedule.every(1).minutes.do(get_data)

while True:
    schedule.run_pending()
    time.sleep(1)
