import serial
import time
import os
import sys
import globalserial as gc
#arduino = serial.Serial("/dev/ttyACM0", 9600)
print("PIN 13 = HIGH")
gc.arduino.write(str.encode('9'))
#while True:
	#print("PIN 13 = HIGH")
	#gc.arduino.write(str.encode('9'))
	#time.sleep(5)
	
#arduino.close()