#!/bin/sh

python "/home/pi/Desktop/envmonitor/sensors/mainInflux.py"

echo "Script executed on" $(date) >> influxOutput.log 2>&1
