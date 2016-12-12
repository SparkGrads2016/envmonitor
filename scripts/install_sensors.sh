#!/bin/bash
# installing all sensor drivers

cd ..
sudo mkdir install_files
cd install_files

sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus git



#Adafruit GPIO - covers SHT31-D temp and humidity sensor
sudo git clone  https://github.com/ralf1070/Adafruit_Python_SHT31.git
sudo git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
tempINS=$?
cd ..

#TSL2561 Lux sensor
sudo git clone https://github.com/mgaggero/Adafruit_Python_TSL2561.git
cd Adafruit_Python_TSL2561
sudo python setup.py install
luxINS=$?
cd ..

#BMP180 Barometric pressure, altitude and temperature sensor
sudo git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
pressINS=$?
cd ..

#Sl1145 UV sensor
sudo git clone https://github.com/THP-JOE/Python_SI1145.git
cd Python_SI1145
sudo python setup.py install
uvINS=$?
cd ..

#LSM303 Compass and Accelerometer
sudo git clone https://github.com/adafruit/Adafruit_Python_LSM303.git
cd Adafruit_Python_LSM303
sudo python setup.py install
gyroINS=$?
cd ..

printf "\n\n"
if [ $tempINS -eq 0 ]; then
        echo "SHT31-D Temp sensor install ... OK"
else
        echo "SHT31-D Temp sensor install ... FAIL"
fi

if [ $luxINS -eq 0 ]; then
        echo "TSL2561 Lux sensor install ... OK"
else
        echo "TSL2561 Lux sensor install ... FAIL"
fi

if [ $pressINS -eq 0 ]; then
        echo "BMP180 Pressure sensor install ... OK"
else
        echo "BMP180 Pressure sensor install ... FAIL"
fi

if [ $uvINS -eq 0 ]; then
        echo "SI1145 UV sensor install ... OK"
else
        echo "SI1145 UV sensor install ... FAIL"
fi

if [ $gyroINS -eq 0 ]; then
        echo "LSM303 Accelerometer install ... OK"
else
        echo "LSM303 Accelerometer install ... FAIL"
fi

