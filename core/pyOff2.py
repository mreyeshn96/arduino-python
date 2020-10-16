import serial
import time
import os
import sys
import globalserial as gc
print("PIN 2 = LOW")
#arduino.flushInput()
#arduino.flushOutput()
gc.arduino.write(str.encode('4'))