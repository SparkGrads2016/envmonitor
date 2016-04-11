import RPi.GPIO as GPIO
import time

sensor = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False
counter = 0
seconds = 1

while True:
    time.sleep(0.1)
    counter += 1
    previous_state = current_state
    current_state = GPIO.input(sensor)

    # Print every second
    if counter == 10:
        print("No motion detected for %d seconds" % seconds)
        seconds += 1
        counter = 0

    #print("GPIO pin %s is %s" % (sensor, current_state))

    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        #print("GPIO pin %s is %s" % (sensor, new_state))
        print("Motion detected")

        seconds = 1
        counter = 0
