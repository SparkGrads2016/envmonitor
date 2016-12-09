#!/bin/bash
# testing all sensor 

cd ../.. #change into sensor modules directory

printf "TESTING SENSORS...\n" 
#Adafruit GPIO mod - covers the moduel install of SHT31-D temp and humidity sensor
cd Adafruit_Python_SHT31
sudo python Adafruit_SHT31_Example.py > /dev/null 2>&1 #> /dev/null 2>&1 hides output
temp=$?
cd ..

#TSL2561 Lux sensor
cd Adafruit_Python_TSL2561
cd examples
sudo python simpletest.py > /dev/null 2>&1
lux=$?
cd ../..

#BMP180 Barometric pressure, altitude and temperature sensor
cd Adafruit_Python_BMP
cd examples
sudo python simpletest.py > /dev/null 2>&1

press=$?
cd ../..

#Sl1145 UV sensor
cd Python_SI1145
cd examples
sudo python simpletest.py > /dev/null 2>&1
UV=$?
cd ../..

#LSM303 Compass and Accelerometer
cd Adafruit_Python_LSM303
cd examples
sudo python simpletest.py > /dev/null 2>&1
gyro=$?
cd ../..

if [ $temp -eq 0 ]; then
        echo SHT31-D Temp sensor ... OK
else
        echo SHT31-D Temp sensor ... FAIL
fi


if [ $lux -eq 0 ]; then
        echo TSL2561 Lux sensor ... OK
else
        echo TSL2561 Lux sensor ... FAIL
fi


if [ $press -eq 0 ]; then
        echo BMP180 Pressure sensor ... OK
else
        echo BMP180 Pressure sensor ... FAIL
fi


if [ $UV -eq 0 ]; then
        echo SI1145 UV sensor ... OK
else
        echo SI1145 UV sensor ... FAIL
fi


if [ $gyro -eq 0 ]; then
        echo LSM303 Gyro sensor ... OK
else
        echo LSM303 Gyro sensor ... FAIL
fi 

printf "...TESTING DONE\n"
