#!/bin/bash
echo 0 > /home/reyes/Documentos/GitHub/arduino-python/core/state_arduino_pin13.txt
pkill -f pyOn13.py &
chmod 777 /home/reyes/Documentos/GitHub/arduino-python/core/pyOff13.py 
python3 /home/reyes/Documentos/GitHub/arduino-python/core/pyOff13.py &
pkill -f pyOff13.py &
#echo "PIN 13 (LED ROJO) SE HA APAGADO." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com