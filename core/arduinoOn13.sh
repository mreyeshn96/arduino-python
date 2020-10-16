#!/bin/bash
#chmod 777 /home/reyes/Documentos/GitHub/arduino-python/core/pyOn13.py
echo 1 > /home/reyes/Documentos/GitHub/arduino-python/core/state_arduino_pin13.txt
python3 /home/reyes/Documentos/GitHub/arduino-python/core/pyOn13.py &
pkill -f pyOff13.py &
sleep 1
#pkill -f pyOn13.py
#echo "PIN 13 (LED ROJO) SE HA ENCENDIDO." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com