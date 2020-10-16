#!/bin/bash
echo 0 > /home/reyes/Documentos/GitHub/arduino-python/core/state_arduino_examen.txt
pkill -f pyExamenOn.py &
#chmod 777 /home/reyes/Documentos/GitHub/arduino-python/core/pyOff2.py
python3 /home/reyes/Documentos/GitHub/arduino-python/core/pyExamenOff.py &
pkill -f pyExamenOff.py &
echo "EXAMEN - OFF." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com