import lightSensor as light
#import tempHumSensor as tempHum
import baroTempAltSensor as BTA
import uvSensor as uv
import SI1145.SI1145 as SI1145
import accelMagSensor as accelMag
import windSensor as wind
import RPi.GPIO as GPIO
import time
from time import strftime
from ConfigParser import SafeConfigParser

# Sensor pins
pinTempHum = 18 # Set the TempHum pin
adcWind = 0     # Set the pin on the ADC getting wind speed

sensor = SI1145.SI1145()
#si1145 = uv.initUV()

# Use to convert the accelerometer readings into m/s^2
metreConst_x = 103.60
metreConst_y = 104.70
metreConst_z = 101.85

# Set how often the monitor will output data
sleepTime = 3.0

# LED pin mapping
ledRed = 21
ledGreen = 20

# LED setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledRed,GPIO.OUT)
GPIO.setup(ledGreen,GPIO.OUT)
GPIO.output(ledRed,GPIO.LOW)
GPIO.output(ledGreen,GPIO.LOW)

# Turns the green LED on for 1 second
def sendSuccess():
        GPIO.output(ledGreen,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(ledGreen,GPIO.LOW)

# Turns the red LED on for 1 second
def sendFailure():
        GPIO.output(ledRed,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(ledRed,GPIO.LOW)

# Initialise config parser and read in the config file 'envMonitorSettings.ini'
parser = SafeConfigParser()
parser.read('envMonitorSettings.ini')

# For debugging. Prints out the contents of the config file
#for section_name in parser.sections():
#    print 'Section:', section_name
#    print '  Options:', parser.options(section_name)
#    for name, value in parser.items(section_name):
#        print '  %s = %s' % (name, value)

# Check if section in config file exists
if parser.has_section('sensors'):
	print ('Section correct')
else:
	print ('Section in config file does not appear to exist')

# Process start time
t0 = time.time()

# The string to output
sensorPrint = ''

# Loop through 'sensors' part of config file and extract data from all sensors selected
for sensorName,sensorValue in parser.items('sensors'):
	#print '  %s = %s' % (sensorName, sensorValue)
	
	# Output type
	if (sensorName == 'outputtype'):
		print ('Output Type specified')
		sensorPrint += sensorValue
	if (sensorName == 'location'):
		print ('Location specified')
		sensorPrint += ',location=' + sensorValue + ' '
	# Acceleration
	if (sensorName == 'acceleration') and (sensorValue == 'true'):
		print ('* Acceleration found')
		accel = accelMag.getAccel()
		accel_x, accel_y, accel_z = accel
		sensorPrint += ('accelX={0:0.2f},accelY={1:0.2f},accelZ={2:0.2f}'.format(accel_x/metreConst_x, accel_y/metreConst_y, accel_z/metreConst_z))
	elif (sensorName == 'acceleration') and (sensorValue == 'false'):
		print ('* No Acceleration output')
	# Altitude
	if (sensorName == 'altitude') and (sensorValue == 'true'):
		print ('* Alitude found')
		altitude = BTA.getAltitude()
		sensorPrint += (',altitude={0:0.2f}'.format(altitude))
	elif (sensorName == 'altitude') and (sensorValue == 'false'):
		print ('* No Altitude output')
	# Barometric Pressure
	if (sensorName == 'barometricpressure') and (sensorValue == 'true'):
		print ('* Barometric Pressure found')
		pressure = BTA.getPressure()
		sensorPrint += (',barometricPressure={0:0.2f}'.format(pressure))
	elif (sensorName == 'barometricpressure') and (sensorValue == 'false'):
		print ('* No Barometric Pressure output')
	# Full Spectrum
	if (sensorName == 'fullspectrum') and (sensorValue == 'true'):
		print ('* Full Spectrum found')
	elif (sensorName == 'fullspectrum') and (sensorValue == 'false'):
		print ('* No Full Spectrum output')
	# Humidity
	if (sensorName == 'humidity') and (sensorValue == 'true'):
		print ('* Humidity found')
	elif (sensorName == 'humidity') and (sensorValue == 'false'):
		print ('* No Humidity output')
	# IR
	if (sensorName == 'ir') and (sensorValue == 'true'):
		print ('* IR found')
	elif (sensorName == 'ir') and (sensorValue == 'false'):
		print ('* No IR output')
	# Lux (All light)
	if (sensorName == 'lux') and (sensorValue == 'true'):
		print ('* Lux found')
		lux, full, ir = light.getLight()
		sensorPrint += (',lux=%d,fullSpectrum=%d,ir=%d' % (lux, full, ir))
	elif (sensorName == 'lux') and (sensorValue == 'false'):
		print ('* No Lux output')
	# Magnetic Flux
	if (sensorName == 'magneticflux') and (sensorValue == 'true'):
		print ('* Magnetic Flux found')
		mag = accelMag.getMag()
		mag_x, mag_y, mag_z = mag
		sensorPrint += (',magX={0},magY={1},magZ={2}'.format(mag_x, mag_y, mag_z))
	elif (sensorName == 'magneticflux') and (sensorValue == 'false'):
		print ('* No Magnetic Flux output')
	# Sealevel Pressure
	if (sensorName == 'sealevelpressure') and (sensorValue == 'true'):
		print ('* Sealevel Pressure found')
		sealevelPressure = BTA.getSealevelPressure()
		sensorPrint += (',sealevelPressure={0:0.2f}'.format(sealevelPressure))
	elif (sensorName == 'sealevelpressure') and (sensorValue == 'false'):
		print ('* No Sealevel Pressure output')
	# Temperature
	if (sensorName == 'temperature') and (sensorValue == 'true'):
		print ('* Temperature  found')
		temperature = BTA.getTemperature()
		sensorPrint += (',temperature={0:0.2f}'.format(temperature))
	elif (sensorName == 'temperature') and (sensorValue == 'false'):
		print ('* No Temperature output')
	# UV Index
	if (sensorName == 'uvindex') and (sensorValue == 'true'):
		print ('* UV Index found')
		UV = sensor.readUV()
		uvIndex = UV / 100.0
		sensorPrint += (',uvIndex=' + str(uvIndex))
	elif (sensorName == 'uvindex') and (sensorValue == 'false'):
		print ('* No UV Index output')
	# Wind Speed Km (Both Km and m for now)
	if (sensorName == 'windspeedkm') and (sensorValue == 'true'):
		print ('* Wind Speed (Km) found')
		windBits, windVoltage, windSpeedM, windSpeedKm = wind.getWindSpeed(adcWind)
		sensorPrint += (',windSpeedM={0:0.3f},windSpeedKm={1:0.3f}'.format(windSpeedM, windSpeedKm))
	elif (sensorName == 'windspeedkm') and (sensorValue == 'false'):
		print ('* No Wind Speed (Km) output')
	# Wind Speed m
	if (sensorName == 'windspeedm') and (sensorValue == 'true'):
		print ('* Wind Speed (m) found')
	elif (sensorName == 'windspeedm') and (sensorValue == 'false'):
		print ('* No Wind Speed (m) output')
	

# For debugging
#print ('Start of loop Environmental Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S") + '\n')

# Light
#lux, full, ir = light.getLight() #lux, full, ir = light.getLight(tsl2591)
 #uv = uv.getUV(si1145)
#UV = sensor.readUV()
#uvIndex = UV / 100.0

# Temperature and Humidity
#temperature = BTA.getTemperature()
#hum = tempHum.getHum(pinTempHum)

# Barometer and Altometer
#pressure = BTA.getPressure()
#altitude = BTA.getAltitude()
#sealevelPressure = BTA.getSealevelPressure()

# Accelerometer and Magnetometer
#accel = accelMag.getAccel()
#accel_x, accel_y, accel_z = accel
#mag = accelMag.getMag()
#mag_x, mag_y, mag_z = mag
#windBits, windVoltage, windSpeedM, windSpeedKm = wind.getWindSpeed(adcWind)

# Time to sleep
#t1 = time.time()		# Process end time
#t2 = t1 - t0			# Calculate process time to get sensor data
#sleep = sleepTime - t2	# Calculate the difference in specified sleep time and sensor process time
#time.sleep(sleep)		# Sleep for that difference

# Print out variables
#print (strftime("%Y-%m-%d") + ' ' + strftime("%H:%M:%S") + '\n')
#print ('Lux = %d \nFull Spectrum = %d \nIR = %d' % (lux, full, ir))
#print ('UVIndex = ' + str(uvIndex))
#print ('Temperature = {0:0.2f}'.format(temperature))
#print ('Humidity = {0:0.2f}'.format(hum))
#print ('BarometricPressure = {0:0.2f}'.format(pressure))
#print ('Altitude = {0:0.2f}'.format(altitude))
#print ('SealevelPressure = {0:0.2f}'.format(sealevelPressure))
#print ('AccelX = {0:0.2f}\nAccelY = {1:0.2f}\nAccelZ = {2:0.2f}'.format(accel_x/metreConst_x, accel_y/metreConst_y, accel_z/metreConst_z))
#print ('MagX = {0}\nMagY = {1}\nMagZ = {2}'.format(mag_x, mag_y, mag_z))
#print ('WindSpeedM  = {0:0.3f}\nWindSpeedKm = {1:0.3f}'.format(windSpeedM, windSpeedKm))

# For debugging
#print ('End of loop    Now sleeping Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S"))
  
#print ('-----------------------------------------------------------------------------\n')

#sendSuccess()

print (sensorPrint)

# For debugging
t3 = time.time()
print ('Total time = {0}'.format(t3-t0))
