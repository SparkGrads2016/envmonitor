import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
DEBUG = 1

# Changes these variables to the corresponding GPIO pins connected to
# on the Pi
SPICLK = 23	 # CLK
SPIMISO = 24 # Dout
SPIMOSI = 25 # Din
SPICS = 12	 # CS

GPIO.setwarnings(False)

# Set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

# Read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
# Return a bit value ranging from 0 to 1023 (2^10 bits)
def readadc(adcnum):
	if ((adcnum > 7) or (adcnum < 0)):
		return -1
	
	GPIO.output(SPICS, True)
	GPIO.output(SPICLK, False)  # start clock low
	GPIO.output(SPICS, False)     # bring CS low
	
	commandout = adcnum
	commandout |= 0x18  # start bit + single-ended bit
	commandout <<= 3    # we only need to send 5 bits here
	
	for i in range(5):
		if (commandout & 0x80):
			GPIO.output(SPIMOSI, True)
		else:
			GPIO.output(SPIMOSI, False)
		
		commandout <<= 1
		GPIO.output(SPICLK, True)
		GPIO.output(SPICLK, False)
		
	adcout = 0
	# read in one empty bit, one null bit and 10 ADC bits
	for i in range(12):
		GPIO.output(SPICLK, True)
		GPIO.output(SPICLK, False)
		adcout <<= 1
			
		if (GPIO.input(SPIMISO)):
			adcout |= 0x1
				
	GPIO.output(SPICS, True)
		
	adcout >>= 1       # first bit is 'null' so drop it
		
	return adcout
