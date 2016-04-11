import lightSensor
import tempHumSensor
import time

pinTempHum = 24 # Set the TempHum pin
# pinPir = 18     # Set the PIR pin

tsl = lightSensor.initLight() 

while True:
    lux, full, ir = lightSensor.getLight(tsl)
    temp, hum = tempHumSensor.getTempHum(pinTempHum)

    print ('Environmental Readings:')
    print ('Lux = %d \nFull Spectrum = %d \nIR = %d' % (lux, full, ir))
    print ('Temp = {0:0.1f}* \nHumidity = {1:0.1f}%\n'.format(temp, hum))
    
    time.sleep(10.0)
