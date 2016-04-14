import lightSensor as light
import tempHumSensor as tempHum
import time
from time import strftime

pinTempHum = 24 # Set the TempHum pin
# pinPir = 18     # Set the PIR pin

tsl = light.initLight() 

while True:
    lux, full, ir = light.getLight(tsl)
    temp, hum = tempHum.getTempHum(pinTempHum)
    
    print ('Environmental Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S"))
    print ('Lux = %d \nFull Spectrum = %d \nIR = %d' % (lux, full, ir))
    print ('Temp = {0:0.1f}* \nHumidity = {1:0.1f}%\n'.format(temp, hum))
    
    time.sleep(10.0)
