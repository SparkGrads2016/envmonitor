from __future__ import division
import sys
import Adafruit_BMP.BMP085 as BMP085

# Calibrate the altitude to output a value more close to the GPS 
# altitude calculated. This calibrated altitude will be used for 
# pressure and sea level pressure calculations
altOffset = 98.6

# The average sea level pressure. Take this as the reference
sealevelPressure = 101325.0

# The pressure offset for calibration
pressureOffset = 180.0

# The altitude offset for calibration
altitudeOffset = 31.67

def getTemperature():
	temperature = BMP085.BMP085().read_temperature()
	
	if temperature is not None:
		return temperature
	else:
		print 'Failed to get temperature reading.'
		sys.exit(1)
		
def getPressure():
	# Read in the raw pressure
	rawPressure = BMP085.BMP085().read_pressure()
	
	# Calibrate using the pressure offset
	calibratedPressure = rawPressure - pressureOffset
	
	if calibratedPressure is not None:
		return calibratedPressure / 100.0 # Convert to hectopascals
	else:
		print 'Failed to get barometric pressure reading.'
		sys.exit(1)

def getAltitude():
	# Get the pressure and convert to pascals
	pressure = (getPressure() * 100)
	
	# Convert the pressure to altitude using that sea level pressure reference
	rawAltitude = 44330.0 * (1.0 - pow(pressure / sealevelPressure, (1.0/5.255)))
	
	# Calibrate the altitude value
	calibratedAltitude = rawAltitude - altitudeOffset
	
	if calibratedAltitude is not None:
		return calibratedAltitude
	else:
		print 'Failed to get altitude reading.'
		sys.exit(1)
		
def getSealevelPressure():
    # Get the pressure and convert to pascals, also get the altitude
	pressure = getPressure() * 100
	altitude = getAltitude()
	
	# Use the the pressure and altitude to calculate the sealevel pressure
	sealevelPressure = pressure / pow(1.0 - altitude/44330.0, 5.255)
	
	if sealevelPressure is not None:
		return sealevelPressure / 100.0 # Convert to hectopascals
	else:
		print 'Failed to get sealevel pressure reading.'
		sys.exit(1)
