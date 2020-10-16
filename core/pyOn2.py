import serial
import time
import os
import sys
import globalserial as gc
#arduino = serial.Serial("/dev/ttyACM0", 9600)
print("PIN 2 = HIGH")
gc.arduino.write(str.encode('5'))
#while True:
	#print("PIN 2 = HIGH")
	#gc.arduino.write(str.encode('5'))
	#time.sleep(5)
	
#arduino.close()