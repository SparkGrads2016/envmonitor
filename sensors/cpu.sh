#! /bin/sh
TIME=$(date +"%D %T.%3N %Z")
VOLTS=$(vcgencmd measure_volts)
TEMP=$(vcgencmd measure_temp)
RAM=$(vcgencmd get_mem arm)
GPU=$(vcgencmd get_mem gpu)

VOLTS=`echo $VOLTS | cut -d V -f 1`
CPU_TEMP=`echo $TEMP | cut -d \' -f 1`
RAM=`echo $RAM | cut -d M -f 1`
GPU=`echo $GPU | cut -d M -f 1`

echo "time=$TIME"
echo "$VOLTS"
echo "$CPU_TEMP"
echo "$RAM"
echo "$GPU"

free -m | awk 'NR==2{printf "MemoryUsage: %s/%sMB (%.2f%%)\n", $3, $2, $3*100/$2}'
df -h -m | awk 'NR==2{printf "DiskUsage: Used: %sMB Available: %sMB InUse: %s\n", $3,$4,$5}'
# This only tkaes one CPU load. Maybe average the three
top -bn1 | grep load | awk '{printf "CPULoad: %.2f\n", $(NF-2)}'