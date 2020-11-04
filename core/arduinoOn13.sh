#!/bin/bash
user=`cut -d " " -f1 /home/reyes/.conexion.txt`
pass=`cut -d " " -f2 /home/reyes/.conexion.txt`
db=`cut -d " " -f3 /home/reyes/.conexion.txt`
fecha=`date +"%Y-%m-%d-%T"`
usuario="Franklin Reyes"

query="INSERT INTO action(num_pin, value, fecha, usuario) VALUES ('13', '1', '$fecha', '$usuario')"
mysql -u root -p$pass $db -e "$query"

#chmod 777 /home/reyes/Documentos/GitHub/arduino-python/core/pyOn13.py
cd /home/reyes/Documentos/GitHub/arduino-python
echo 1 > core/state_arduino_pin13.txt
python3 core/pyOn13.py &
pkill -f pyOff13.py &
sleep 1
#pkill -f pyOn13.py
#echo "PIN 13 (LED ROJO) SE HA ENCENDIDO." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com