import lightSensor as light
import tempHumSensor as tempHum
import baroTempAltSensor as BTA
import uvSensor as uv
import SI1145.SI1145 as SI1145
import accelMagSensor as accelMag
import windSensor as wind
import RPi.GPIO as GPIO
import math
import time
from time import strftime
from ConfigParser import SafeConfigParser

# Use to convert the accelerometer readings into m/s^2
metreConst_x = 103.60
metreConst_y = 104.70
metreConst_z = 101.85

# Initialise UV sensor
sensor = SI1145.SI1145()

def altitude():
	altitude = BTA.getAltitude()
	return (',altitude={0:0.2f}'.format(altitude))

def parseSensor(sensorName,sensorValue):
	# Output type
	if (sensorName == 'outputtype'):
		return sensorValue
	# Time
	if (sensorName == 'time'):
		return (',time=' + strftime("%H:%M:%S"))
	# Date
	if (sensorName == 'date'):
		return (',date=' + strftime("%d/%m/%Y"))
	# Location
	if (sensorName == 'location'):
		return (',location=' + sensorValue + ' ')
	# Acceleration
	if (sensorName == 'acceleration') and (sensorValue == 'true'):
		accel = accelMag.getAccel()
		accel_x, accel_y, accel_z = accel
		return (',accelX={0:0.2f},accelY={1:0.2f},accelZ={2:0.2f}'.format(accel_x/metreConst_x, accel_y/metreConst_y, accel_z/metreConst_z))
	# Altitude
	if (sensorName == 'altitude') and (sensorValue == 'true'):
		altitude = BTA.getAltitude()
		return (',altitude={0:0.2f}'.format(altitude))
	# Barometric pressure
	if (sensorName == 'barometricpressure') and (sensorValue == 'true'):
		pressure = BTA.getPressure()
		return (',barometricPressure={0:0.2f}'.format(pressure))
	# Humidity
	if (sensorName == 'humidity') and (sensorValue == 'true'):
		humidity = tempHum.getHum()
		return (',humidity={0:0.2f}'.format(humidity))
	# IR
	if (sensorName == 'ir') and (sensorValue == 'true'):
		infra = light.getIR()
		return (',infrared={:d}'.format(infra))
	# visible light
        if (sensorName == 'vislight') and (sensorValue == 'true'):
                vislight = light.getVislight()
                return (',visiblelight={:d}'.format(vislight))
	# lux
        if (sensorName == 'lux') and (sensorValue == 'true'):
                lux = light.getLux()
                return (',lux={:d}'.format(lux))
	#if (sensorName == 'lux') and (sensorValue == 'true'):
	#	lux, vislight, infra = light.getLight()
	#	return (',lux=%d,vislight=%d' % (lux, vislight, infra))
	# Magnetic Flux
	if (sensorName == 'magneticflux') and (sensorValue == 'true'):
		mag = accelMag.getMag()
                mag_x, mag_z, mag_y = mag
               
		bearing = (math.atan2(mag_y, mag_x) * 180) / math.pi
                if (bearing < 0):
                        bearingAdj = 360 + int(bearing)
                else:
                        bearingAdj = int(bearing)
                return (',magX={0},magZ={1},magY={2},bearing={3}'.format(mag_x, mag_z, mag_y, bearingAdj))
	# Sealevel Pressure
	if (sensorName == 'sealevelpressure') and (sensorValue == 'true'):
		sealevelPressure = BTA.getSealevelPressure()
		return (',sealevelPressure={0:0.2f}'.format(sealevelPressure))
	# Temperature
	if (sensorName == 'temperature') and (sensorValue == 'true'):
		temperature = tempHum.getTemp()
                return (',temperature={0:0.2f}'.format(temperature))
	# UV Index
	if (sensorName == 'uvindex') and (sensorValue == 'true'):
		#si1145 = uv.initUV()
		UV = sensor.readUV()
		uvIndex = UV / 100.0
		return (',uvIndex=' + str(uvIndex))
	# Wind Speed Km (Both Km and m for now)
	if (sensorName == 'windspeedkm') and (sensorValue == 'true'):
		adcWind = 0     # Set the pin on the ADC getting wind speed
		windBits, windVoltage, windSpeedM, windSpeedKm = wind.getWindSpeed(adcWind)
		return (',windSpeedM={0:0.3f},windSpeedKm={1:0.3f}'.format(windSpeedM, windSpeedKm))
	# Wind Speed m
	if (sensorName == 'windspeedm') and (sensorValue == 'true'):
		return ('')
