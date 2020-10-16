import serial
import time
import os
import sys
import globalserial as gc
print("EXAMEN  = HIGH")

gc.arduino.write(str.encode('1'))