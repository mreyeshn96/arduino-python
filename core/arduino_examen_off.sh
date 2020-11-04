#!/bin/bash
echo 0 > core/state_arduino_examen.txt
pkill -f pyExamenOn.py &
#chmod 777 core/pyOff2.py
python3 core/pyExamenOff.py &
pkill -f pyExamenOff.py &
#echo "EXAMEN - OFF." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com