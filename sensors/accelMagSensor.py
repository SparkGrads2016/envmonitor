import Adafruit_LSM303
import math
import sys

# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()
	
# Get the accelerometer reading	
def getAccel():
	# Read the X, Y, Z axis acceleration values
	accel, mag = lsm303.read()
    
	if accel is not None:
		return accel
	else: 
		print 'Failed to get accelerometer reading.'
		sys.exit(1)

# Get the magnetometer reading		
def getMag():
	# Read the X, Y, Z axis magnetometer values
	accel, mag = lsm303.read()
    
	if mag is not None:
		return mag
	else: 
		print 'Failed to get accelerometer reading.'
		sys.exit(1)
