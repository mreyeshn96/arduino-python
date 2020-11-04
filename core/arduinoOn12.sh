#!/bin/bash
user=`cut -d " " -f1 /home/reyes/.conexion.txt`
pass=`cut -d " " -f2 /home/reyes/.conexion.txt`
db=`cut -d " " -f3 /home/reyes/.conexion.txt`
fecha=`date +"%Y-%m-%d-%T"`
usuario="Franklin Reyes"
query="INSERT INTO action(num_pin, value, fecha, usuario) VALUES ('12', '1', '$fecha', '$usuario')"
mysql -u root -p$pass $db -e "$query"

cd /home/reyes/Documentos/GitHub/arduino-python
echo 1 > core/state_arduino_pin12.txt
chmod 777 core/pyOn12.py 
python3 core/pyOn12.py &
sleep 1
#pkill -f pyOn2.py
#echo "PIN 13 (LED ROJO) SE HA ENCENDIDO." | mail -s "Notificacion de Arduino" reyes1996.hn@gmail.com