import sys
import Adafruit_TSL2561.TSL2561 as TSL2561

luxsensor = TSL2561.TSL2561()

def getLux():

    lux = luxsensor.read_lux()

    if lux is not None:
        return lux
    else:
        print 'Failed to get lux  reading.'
        sys.exit(1)

def getVislight():

    vislight = luxsensor.read_raw_luminosity()

    if vislight is not None:
        return vislight
    else:
        print 'Failed to get visible light reading.'
        sys.exit(1)

def getIR():

    infra = luxsensor.read_raw_luminosity()

    if infra is not None:
        return infra
    else:
        print 'Failed to get IR reading.'
        sys.exit(1)




