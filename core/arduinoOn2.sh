#!/bin/bash
echo 1 > /home/reyes/Documentos/GitHub/arduino-python/core/state_arduino_pin2.txt
chmod 777 /home/reyes/Documentos/GitHub/arduino-python/core/pyOn2.py 
python3 /home/reyes/Documentos/GitHub/arduino-python/core/pyOn2.py &
sleep 1
#pkill -f pyOn2.py
#echo "PIN 13 (LED ROJO) SE HA ENCENDIDO." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com