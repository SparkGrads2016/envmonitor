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

#echo "time=$TIME"
#echo "$VOLTS"
#echo "$CPU_TEMP"
#echo "$RAM"
#echo "$GPU"

#free -m | awk 'NR==2{printf "MemoryUsage: %s/%sMB (%.2f%%)\n", $3, $2, $3*100/$2}'
#df -h -m | awk 'NR==2{printf "DiskUsage: Used: %sMB Available: %sMB InUse: %s\n", $3,$4,$5}'
# This only tkaes one CPU load. Maybe average the three
#top -bn1 | grep load | awk '{printf "CPULoad: %.2f\n", $(NF-2)}'

MEM_USED=$(free -m | awk 'NR==2{printf "%s", $3}')
MEM_FREE=$(free -m | awk 'NR==2{printf "%s", $2-$3}')
DISK_USED=$(df -h -m | awk 'NR==2{printf "%s", $3}')
DISK_FREE=$(df -h -m | awk 'NR==2{printf "%s", $4}')
CPU_LOAD=$(top -bn1 | grep load | awk '{printf "%.2f\n", $(NF-2)}')

echo monitorInternal,location=richardDesk $VOLTS,$CPU_TEMP,$RAM,$GPU,memUsed=$MEM_USED,memFree=$MEM_FREE,diskUsed=$DISK_USED,diskFree=$DISK_FREE,cpuLoad=$CPU_LOAD
