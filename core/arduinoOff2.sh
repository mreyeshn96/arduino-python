#!/bin/bash
user=`cut -d " " -f1 /home/reyes/.conexion.txt`
pass=`cut -d " " -f2 /home/reyes/.conexion.txt`
db=`cut -d " " -f3 /home/reyes/.conexion.txt`
fecha=`date +"%Y-%m-%d-%T"`
usuario="Franklin Reyes"

query="INSERT INTO action(num_pin, value, fecha, usuario) VALUES ('2', '0', '$fecha', '$usuario')"
mysql -u root -p$pass $db -e "$query"

cd /home/reyes/Documentos/GitHub/arduino-python
echo 0 > core/state_arduino_pin2.txt
pkill -f pyOn2.py &
#chmod 777 core/pyOff2.py
python3 core/pyOff2.py &
pkill -f pyOff2.py &
#echo "PIN 2 (LED ROJO) SE HA APAGADO." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com