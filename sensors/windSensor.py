import ADC
import time

# Change these to constants/defines
bitMin = 125 # Corresponds to 0.4V (0m/s)
bitMax = 621 # Corresponds to 2V (32.4m/s)
bitRange = bitMax - bitMin

speedMax = 32.4
speedConst = speedMax/bitRange

def getWindSpeed(adc_pin):
	# Read the ADC pin
	windBits = ADC.readadc(adc_pin)
	
	# Get the 8-bit (voltage) output. Range from 0 to 1023
	bits = int(windBits)
	
	# Convert the ADC output to a voltage value
	if (bits < bitMin):
		voltage = 0.4
	elif (bits > bitMax):
		voltage = 2
		print ('Voltage at maximum, maximum wind speed reached\n')
	else:
		voltage = ((bits * 3.3) / 1024)
		
	# Shift bits for speed calculation
	bitShift = bits - bitMin
		
	# Speed is 0m/s
	if (bitShift < 0):
		bitShift = 0
			
	speedM = speedConst * bitShift # Speed increases linearly
	speedKm = speedM * 3.6		   # Convert from metres to kilometres
	
	return bits, voltage, speedM, speedKm
