import sys
import tsl2591

# Initialise the light sensor
def initLight():
    tsl = tsl2591.Tsl2591()  # initialise
    return tsl

# Return the lux, full spectrum and IR light
def getLight(tsl):
    full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
    lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
    
    if lux is not None and full is not None and ir is not None:
        return lux, full, ir
    else:
        print 'Failed to get light reading.'
        sys.exit(1)
