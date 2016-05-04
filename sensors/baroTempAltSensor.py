import sys
import Adafruit_BMP.BMP085 as BMP085

def getTemp():
	temp = BMP085.BMP085().read_temperature()
	
	if temp is not None:
		return temp
	else:
		print 'Failed to get temperature reading.'
		sys.exit(1)
		
def getBaro():
	baro = BMP085.BMP085().read_pressure()
	baro = baro / 100.0 # Convert to hectopascals
	
	if baro is not None:
		return baro
	else:
		print 'Failed to get barometric pressure reading.'
		sys.exit(1)

def getAlt():
	alt = BMP085.BMP085().read_altitude()
	
	if alt is not None:
		return alt
	else:
		print 'Failed to get altitude reading.'
		sys.exit(1)
		
def getSeaPres():
	seaPres = BMP085.BMP085().read_sealevel_pressure()
	seaPres = seaPres / 100.0 # Convert to hectopascals
	
	if seaPres is not None:
		return seaPres
	else:
		print 'Failed to get sealevel pressure reading.'
		sys.exit(1)
