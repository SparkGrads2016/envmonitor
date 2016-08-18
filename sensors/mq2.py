import ADC
import time

# Change these to constants/defines
bitMin = 125 				# Corresponds to 0.4V (0m/s)
bitMax = 621				# Corresponds to 2V (32.4m/s)
bitRange = bitMax - bitMin

speedMax = 32.4
speedConst = speedMax/bitRange # The speed of one bit

def getWindSpeed(adc_pin):
	# Read the ADC pin
	windBits = ADC.readadc(adc_pin)
	
	# Get the 8-bit (voltage) output. Range from 0 to 1023
	bits = int(windBits)
	
	# Convert the ADC output to a voltage value
	# If the ADC reading is above or below the expected threshold values
	# set them to the threshold values. Else calculate as normal
	if (bits < bitMin):
		voltage = 0.4
	elif (bits > bitMax):
		voltage = 2
		print ('Voltage at maximum, maximum wind speed reached\n')
	else:
		voltage = ((bits * 3.3) / 1024)
		
	# Shift bits for speed calculation. This is the actual increase in
	# speed (bits) as the anemometer will output a base of 125 bits (0.4V)
	# when not moving
	bitShift = bits - bitMin
		
	# If bitShift result is less than 0, change to 0 before wind speed
	# calculation
	if (bitShift < 0):
		bitShift = 0
	
	# As the increase in speed is linear, multiply the number of bits by
	# the speed constant
	speedM = speedConst * bitShift # Speed increases linearly
	speedKm = speedM * 3.6		   # Convert from metres to kilometres
	
	return bits, voltage, speedM, speedKm


def getMQ2(adc_pin):
        # Read the ADC pin
        mq2Bits = ADC.readadc(adc_pin)

        # Get the 8-bit (voltage) output. Range from 0 to 1023
        bits = int(mq2Bits)

	return bits

while True:
	adcWind = 0     # Set the pin on the ADC getting wind speed
	adcMQ2 = 1
	
	windBits, windVoltage, windSpeedM, windSpeedKm = getWindSpeed(adcWind)
	print ('bits={0},voltage={1:0.3f},windSpeedM={2:0.3f},windSpeedKm={3:0.3f}'.format(windBits,windVoltage,windSpeedM, windSpeedKm))
	
#	mq2Reading = ADC.readadc(adcMQ2)
#	print ('Bits = {0}'.format(mq2Reading))
	
	time.sleep(1.0)
