#import lightSensor as light
import tempHumSensor as tempHum
import baroTempAltSensor as BTA
import uvSensor as uv
import SI1145.SI1145 as SI1145
import accelMagSensor as accelMag
import windSensor as wind
import RPi.GPIO as GPIO
import time
from time import strftime

# Sensor pins
pinTempHum = 18 # Set the TempHum pin
adcWind = 0	# Set the pin on the ADC getting wind speed

#tsl2591 = light.initLight() 
sensor = SI1145.SI1145()
#si1145 = uv.initUV()

# Use to convert the accelerometer readings into m/s^2
metreConst_x = 103.60
metreConst_y = 104.70
metreConst_z = 101.85

# Set how often the monitor will output data
sleepTime = 4.0

# LED pin mapping
ledBlue = 17
ledGreen = 27

# LED setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledBlue,GPIO.OUT)
GPIO.setup(ledGreen,GPIO.OUT)
GPIO.output(ledGreen,GPIO.LOW)

#GPIO.output(ledBlue,GPIO.HIGH)
#time.sleep(1.0)
#GPIO.output(ledBlue,GPIO.LOW)

def sendSuccess():
	GPIO.output(ledGreen,GPIO.HIGH)
	time.sleep(1.0)
	GPIO.output(ledGreen,GPIO.LOW)

# Process start time
t0 = time.time()

# For debugging
#print ('Start of loop Environmental Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S") + '\n')

# Light
#lux, full, ir = light.getLight(tsl2591)
#uv = uv.getUV(si1145)
UV = sensor.readUV()
uvIndex = UV / 100.0

# Temperature and Humidity
temperature = BTA.getTemperature()
hum = tempHum.getHum(pinTempHum)

# Barometer and Altometer
pressure = BTA.getPressure()
altitude = BTA.getAltitude()
sealevelPressure = BTA.getSealevelPressure()

# Accelerometer and Magnetometer
accel = accelMag.getAccel()
accel_x, accel_y, accel_z = accel
mag = accelMag.getMag()
mag_x, mag_y, mag_z = mag
windBits, windVoltage, windSpeedM, windSpeedKm = wind.getWindSpeed(adcWind)

# Time to sleep
t1 = time.time()		# Process end time
t2 = t1 - t0			# Calculate process time to get sensor data
sleep = sleepTime - t2	# Calculate the difference in specified sleep time and sensor process time
time.sleep(sleep)		# Sleep for that difference

# Print out variables
print (strftime("%Y-%m-%d") + ' ' + strftime("%H:%M:%S") + '\n')
#print ('Lux = %d \nFull Spectrum = %d \nIR = %d' % (lux, full, ir))
print ('UVIndex = ' + str(uvIndex))
print ('Temperature = {0:0.2f}'.format(temperature))
print ('Humidity = {0:0.2f}'.format(hum))
print ('BarometricPressure = {0:0.2f}'.format(pressure))
print ('Altitude = {0:0.2f}'.format(altitude))
print ('SealevelPressure = {0:0.2f}'.format(sealevelPressure))
print ('AccelX = {0:0.2f}\nAccelY = {1:0.2f}\nAccelZ = {2:0.2f}'.format(accel_x/metreConst_x, accel_y/metreConst_y, accel_z/metreConst_z))
print ('MagX = {0}\nMagY = {1}\nMagZ = {2}\n'.format(mag_x, mag_y, mag_z))
print ('WindSpeedM  = {0:0.3f}\nWindSpeedKm = {1:0.3f}'.format(windSpeedM, windSpeedKm))

GPIO.output(ledGreen, GPIO.HIGH)
time.sleep(1.0)
GPIO.output(ledGreen, GPIO.LOW)

# For debugging
#print ('End of loop    Now sleeping Readings on ' + strftime("%Y-%m-%d") + ' at ' + strftime("%H:%M:%S"))
  
#print ('-----------------------------------------------------------------------------\n')

#sendSuccess()

# For debugging
#t3 = time.time()
#print ('Total time = {0}'.format(t3-t0))
