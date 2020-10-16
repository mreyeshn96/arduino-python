#!/bin/bash
echo 0 > /home/reyes/Documentos/GitHub/arduino-python/core/state_arduino_pin2.txt
pkill -f pyOn2.py &
#chmod 777 /home/reyes/Documentos/GitHub/arduino-python/core/pyOff2.py
python3 /home/reyes/Documentos/GitHub/arduino-python/core/pyOff2.py &
pkill -f pyOff2.py &
#echo "PIN 2 (LED ROJO) SE HA APAGADO." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com