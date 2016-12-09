#!/bin/bash
# installing all sensor drivers
 

sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git

#Adafruit GPIO - covers SHT31-D temp and humidity sensor
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
$TempINS = $?
cd ..

#TSL2561 Lux sensor
git clone https://github.com/mgaggero/Adafruit_Python_TSL2561.git
cd Adafruit_Python_TSL2561
sudo python setup.py install
$LuxINS = $?
cd ..

#BMP180 Barometric pressure, altitude and temperature sensor
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
$PressureINS = $?
#cd examples
#sudo python simpletest.py
#cd ..
cd ..

#Sl1145 UV sensor
git clone https://github.com/THP-JOE/Python_SI1145.git
cd Python_SI1145
sudo python setup.py install
$UvINS = $?
#cd examples
#sudo python simpletest.py
cd ..


#LSM303 Compass and Accelerometer
sudo apt-get update
git clone https://github.com/adafruit/Adafruit_Python_LSM303.git
cd Adafruit_Python_LSM303
sudo python setup.py install
$GyroINS = $?
cd ..
