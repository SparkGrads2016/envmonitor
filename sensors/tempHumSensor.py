import sys
from Adafruit_SHT31 import *

SHT31 = SHT31(address = 0x044)

def getTemp():
    temperature = SHT31.read_temperature()

    SHT31.clear_status()
    SHT31.set_heater(True)

    SHT31.set_heater(False)
    
    if temperature is not None:
        return temperature
    else:
	print 'Failed to get temperature reading.'
	sys.exit(1)

def getHum():
    humidity = SHT31.read_humidity()

    SHT31.clear_status()
    SHT31.set_heater(True)

    SHT31.set_heater(False)

    if humidity is not None:
        return humidity
    else:
        print 'Failed to get humidity reading.'
        sys.exit(1)
