import tsl2591
import time

tsl = tsl2591.Tsl2591()  # initialize

while True:
    full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
    lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
    print('Lux=%d, Full Spectrum=%d, IR=%d' % (lux, full, ir))
    
    time.sleep(1.0)
