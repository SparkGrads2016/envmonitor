import lightSensor as light
import tempHumSensor as tempHum
import baroTempAltSensor as BTA
import uvSensor as uv
import SI1145.SI1145 as SI1145
import accelMagSensor as accelMag
import windSensor as wind
import time
from time import strftime

pinTempHum = 18 # Set the TempHum pin
adcWind = 0		# Set the pin on the ADC getting wind speed

tsl2591 = light.initLight() 
sensor = SI1145.SI1145()
si1145 = uv.initUV()

# Use to convert the accelerometer readings into m/s^2
metreConst = 101.8

while True:
	
    print ('Start of loop Environmental Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S") + '\n')
    
    # Light
    lux, full, ir = light.getLight(tsl2591)
    #uv = uv.getUV(si1145)
    UV = sensor.readUV()
    uvIndex = UV / 100.0
    
    # Temperature and Humidity
    temp = BTA.getTemp()
    hum = tempHum.getHum(pinTempHum)
    
    # Barometer and Altometer
    baro = BTA.getBaro()
    alt = BTA.getAlt()
    seaPres = BTA.getSeaPres()
    
    # Accelerometer and Magnetometer
    accel = accelMag.getAccel()
    accel_x, accel_y, accel_z = accel
    mag = accelMag.getMag()
    mag_x, mag_y, mag_z = mag
    windBits, windVoltage, windSpeedM, windSpeedKm = wind.getWindSpeed(adcWind)
    
    # Print out variables
    print ('Lux = %d \nFull Spectrum = %d \nIR = %d' % (lux, full, ir))
    print ('UV Index = ' + str(uvIndex) + '\n')
    print ('Temperature = {0:0.2f}*C'.format(temp))
    print ('Humidity = {0:0.2f}%\n'.format(hum))
    print ('Barometric Pressure = {0:0.2f}hPa'.format(baro))
    print ('Altitude = {0:0.2f}m'.format(alt))
    print ('Sealevel Pressure = {0:0.2f}hPa\n'.format(seaPres))
    print ('Accel X = {0:0.2f}m/s^2  Accel Y = {1:0.2f}m/s^2  Accel Z = {2:0.2f}m/s^2'.format(accel_x/metreConst, accel_y/metreConst, accel_z/metreConst))
    print ('Mag   X = {0}        Mag   Y = {1}        Mag   Z = {2}\n'.format(mag_x, mag_y, mag_z))
    print ('Bits = {0} Voltage = {1:0.2f}V Wind Speed  = {2:0.3f}m/s Wind Speed = {3:0.3f}km/h\n'.format(windBits, windVoltage, windSpeedM, windSpeedKm))
    
    print ('End of loop    Now sleeping Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S"))
    
    print ('\n-----------------------------------------------------------------------------\n')
    
    time.sleep(10.0) # Change number to alter how often monitor gets information in seconds
