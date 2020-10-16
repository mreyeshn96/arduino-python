import serial
import time
import os
import sys
arduino = serial.Serial("/dev/ttyACM0", 9600)
#c = 0
print("PIN 13 = LOW")
#time.sleep(1)
arduino.write(str.encode('8'))
arduino.close()