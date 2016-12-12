#!/bin/bash
# testing all sensor 

cd ../install_files/ #change into sensor modules directory

printf "TESTING SENSORS...\n\n" 
#Adafruit GPIO mod - covers the moduel install of SHT31-D temp and humidity sensor
cd Adafruit_Python_SHT31
sudo python Adafruit_SHT31_Example.py # > /dev/null 2>&1 #> /dev/null 2>&1 hides output
temp=$?
cd ..

printf "\n"

#TSL2561 Lux sensor
cd Adafruit_Python_TSL2561
cd examples
sudo python simpletest.py #> /dev/null 2>&1
lux=$?
cd ../..

printf "\n"


#BMP180 Barometric pressure, altitude and temperature sensor
cd Adafruit_Python_BMP
cd examples
sudo python simpletest.py #> /dev/null 2>&1
press=$?
cd ../..
printf "\n"

#Sl1145 UV sensor
cd Python_SI1145
cd examples
sudo timeout 2s python simpletest.py #> /dev/null 2>&1
UV=$?
cd ../..
printf "\n"

#LSM303 Compass and Accelerometer
cd Adafruit_Python_LSM303
cd examples
sudo timeout 2s python simpletest.py #> /dev/null 2>&1
gyro=$?
cd ../..

printf "\n\n"

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
#the below tests run infinte loops therefore a timeout limit of 2s is used.
#when timeout successfully reaches limit a status code of 124 appears
#tests will never exit with status code 0 as it never fully completes 
if [ $UV -eq 124 ]; then
        echo SI1145 UV sensor ... OK
else
        echo SI1145 UV sensor ... FAIL
fi

if [ $gyro -eq 124 ]; then
        echo LSM303 Accelerometer sensor ... OK
else
        echo LSM303 Accelerometer sensor ... FAIL
fi 

printf "\n...TESTING DONE\n"
