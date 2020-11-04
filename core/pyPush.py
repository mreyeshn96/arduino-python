import serial;
import time;
import os
import threading

arduino = serial.Serial("/dev/ttyACM0", 9600);
filePin7 = open("state_arduino_pin7.txt", "w")
os.system("chmod 777 state_arduino_pin7.txt")

stateFirst = False
lastValue = -1

while True:
    try:
        pushState = arduino.readline().decode(encoding="utf-8")
        #print("Boton pulsado: " + pushState.rstrip('\n'))

        if( lastValue != int(pushState.rstrip('\n')) ):
            
            os.system("echo "+pushState.rstrip('\n')+" > core/state_arduino_pin7.txt")
            time.sleep(1)
            lastValue = int(pushState.rstrip('\n'))
    except:
        pass
    

arduino.close()
filePin7.close()