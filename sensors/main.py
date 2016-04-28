import lightSensor as light
import tempHumSensor as tempHum
import baroTempAltSensor as BTA
#import uvSensor as uv
import SI1145.SI1145 as SI1145
import time
from time import strftime

pinTempHum = 24 # Set the TempHum pin
# pinPir = 18     # Set the PIR pin

tsl = light.initLight() 
sensor = SI1145.SI1145()

while True:
    lux, full, ir = light.getLight(tsl)
    #uv = uv.getUV()
    temp = BTA.getTemp()
    hum = tempHum.getHum(pinTempHum)
    baro = BTA.getBaro()
    alt = BTA.getAlt()
    seaPres = BTA.getSeaPres()
    
    
    UV = sensor.readUV()
    uvIndex = UV / 100.0
    
    print ('Environmental Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S"))
    print ('Lux = %d \nFull Spectrum = %d \nIR = %d' % (lux, full, ir))
    print 'UV Index = ' + str(uvIndex)
    #print 'UV Index = ' + str(UV)
    #print 'UV Index = ' + str(uvIndex)
    #print ('UV Index = {0:0.2f}'.format(uv))
    print ('Temperature = {0:0.2f}*C'.format(temp))
    print ('Humidity = {0:0.2f}%'.format(hum))
    print ('Barometric Pressure = {0:0.2f}Pa'.format(baro))
    print ('Altitude = {0:0.2f}m'.format(alt))
    print ('Sealevel Pressure = {0:0.2f}Pa\n'.format(seaPres))
    
    time.sleep(10.0) # Change number to alter how often monitor gets information in seconds
