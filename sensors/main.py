import lightSensor as light
import tempHumSensor as tempHum
import baroTempAltSensor as BTA
import uvSensor as uv
import SI1145.SI1145 as SI1145
import windSensor as wind
import time
from time import strftime

pinTempHum = 18 # Set the TempHum pin
adcWind = 0		# Set the pin on the ADC getting wind speed

tsl2591 = light.initLight() 
sensor = SI1145.SI1145()
si1145 = uv.initUV()

while True:
	
    print ('Start of loop Environmental Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S") + '\n')
    
    lux, full, ir = light.getLight(tsl2591)
    #uv = uv.getUV(si1145)
    temp = BTA.getTemp()
    hum = tempHum.getHum(pinTempHum)
    baro = BTA.getBaro()
    alt = BTA.getAlt()
    seaPres = BTA.getSeaPres()
    windBits, windVoltage, windSpeedM, windSpeedKm = wind.getWindSpeed(adcWind)
    
    UV = sensor.readUV()
    uvIndex = UV / 100.0
    
    #print (type(uv))
    print (type(uvIndex))
    
    print ('Lux = %d \nFull Spectrum = %d \nIR = %d' % (lux, full, ir))
    print 'UV Index = ' + str(uvIndex)
    #print ('UV Index = {0:0.02f}'.format(uv))

    print ('Temperature = {0:0.2f}*C'.format(temp))
    print ('Humidity = {0:0.2f}%'.format(hum))
    print ('Barometric Pressure = {0:0.2f}Pa'.format(baro))
    print ('Altitude = {0:0.2f}m'.format(alt))
    print ('Sealevel Pressure = {0:0.2f}Pa'.format(seaPres))
    print ('Bits = {0}, Voltage = {1:0.2f}V, Wind Speed  = {2:0.3f}m/s, Wind Speed = {3:0.3f}km/h\n'.format(windBits, windVoltage, windSpeedM, windSpeedKm))
    
    print ('End of loop    Now sleeping Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S"))
    
    print ('\n-----------------------------------------------------------------------------\n')
    
    time.sleep(10.0) # Change number to alter how often monitor gets information in seconds
