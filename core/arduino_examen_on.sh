#!/bin/bash
#chmod 777 /home/reyes/Documentos/GitHub/arduino-python/core/pyOn13.py
echo 1 > /home/reyes/Documentos/GitHub/arduino-python/core/state_arduino_examen.txt
python3 /home/reyes/Documentos/GitHub/arduino-python/core/pyExamenOn.py &
pkill -f pyExamenOff.py &
sleep 1
#pkill -f pyOn13.py
echo "EXAMEN OFF." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com