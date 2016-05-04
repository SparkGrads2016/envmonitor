import sys
import SI1145.SI1145 as SI1145

# Initialise the UV sensor
def initUV():
    si1145 = SI1145.SI1145()  # initialise
    return si1145

def getUV(si1145):
	uv = si1145.readUV()	# Get the raw UV reading
	print (type(uv))
	uvIndex = uv / 100.0 				# Divide raw UV reading by 100 to get the index
	print (type(uvIndex))
	
	if uvIndex is not None:
		return uvIndex
	else:
		print 'Failed to get UV reading.'
		sys.exit(1)
