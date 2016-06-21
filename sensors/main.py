import initSensor as init
import RPi.GPIO as GPIO
import time
from time import strftime
from ConfigParser import SafeConfigParser

# Set how often the monitor will output data
sleepTime = 3.0

# LED pin mapping
ledRed = 21
ledGreen = 20

# LED setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledRed,GPIO.OUT)
GPIO.setup(ledGreen,GPIO.OUT)
GPIO.output(ledRed,GPIO.LOW)
GPIO.output(ledGreen,GPIO.LOW)

# Turns the green LED on for 1 second
def sendSuccess():
        GPIO.output(ledGreen,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(ledGreen,GPIO.LOW)

# Turns the red LED on for 1 second
def sendFailure():
        GPIO.output(ledRed,GPIO.HIGH)
        time.sleep(1.0)
        GPIO.output(ledRed,GPIO.LOW)

# Initialise config parser and read in the config file 'envMonitorSettings.ini'
parser = SafeConfigParser()
parser.read('envMonitorSettings.ini')

# Process start time
t0 = time.time()

# The string to output
sensorPrint = ''

# Loop through 'sensors' part of config file and extract data from all sensors selected
for sensorName,sensorValue in parser.items('sensors'):
	if (sensorValue != 'false'):
		sensorPrint += str(init.parseSensor(sensorName,sensorValue))

sendSuccess()

print (sensorPrint)

# For debugging
t3 = time.time()
print ('Total process time = {0}'.format(t3-t0))
