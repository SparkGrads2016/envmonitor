import sys
import Adafruit_DHT

sensor = 22 #DHT22 sensor

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

#while True:
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
#    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
#    if humidity is not None and temperature is not None:
#        print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
#    else:
#	    print 'Failed to get reading. Try again!'
#	    sys.exit(1)
	    
#    time.sleep(1.0)

def getTempHum(pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
		print 'Failed to get temperature and humidity reading.'
		sys.exit(1)
	
def getTemp(pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        return temperature
    else:
		print 'Failed to get temperature reading.'
		sys.exit(1)

def getHum(pin):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        return humidity
    else:
		print 'Failed to get humidity reading.'
		sys.exit(1)
