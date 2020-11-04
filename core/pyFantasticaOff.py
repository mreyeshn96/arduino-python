import serial
import time
import os
import sys
import globalserial as gc
print("FANTASTIC = LOW")
gc.arduino.write(str.encode('0'))
time.sleep(5)
gc.arduino.write(str.encode('0'))
