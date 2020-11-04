import serial
import time
import os
import sys
#import globalserial as gc
arduino = serial.Serial("/dev/ttyACM0", 9600)

while(True):
    arduino.write(str.encode('9'))
    time.sleep(0.05)
    arduino.write(str.encode('8'))
    arduino.write(str.encode('7'))
    time.sleep(0.05)
    arduino.write(str.encode('6'))
    arduino.write(str.encode('5'))
    time.sleep(0.05)
    arduino.write(str.encode('4'))
    arduino.write(str.encode('3'))
    time.sleep(0.05)
    arduino.write(str.encode('2'))
    #
    arduino.write(str.encode('3'))
    time.sleep(0.05)
    arduino.write(str.encode('2'))
    arduino.write(str.encode('5'))
    time.sleep(0.05)
    arduino.write(str.encode('4'))
    arduino.write(str.encode('7'))
    time.sleep(0.05)
    arduino.write(str.encode('6'))
    arduino.write(str.encode('9'))
    time.sleep(0.05)
    arduino.write(str.encode('8'))

arduino.close()