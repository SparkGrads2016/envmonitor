import sys
import SI1145.SI1145 as SI1145

def getUV():
	
	uv = SI1145.SI1145().readUV()
	uvIndex = uv / 100.0
	#uv = SI1145.SI1145().readUV()	# Get the raw UV reading
	#uvIndex = uv / 100.0 				# Divide raw UV reading by 100 to get the index
	
	if uvIndex is not None:
		return uvIndex
	else:
		print 'Failed to get UV reading.'
		sys.exit(1)
