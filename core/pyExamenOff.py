import serial
import time
import os
import sys
import globalserial as gc

print("EXAMEN = LOW")
gc.arduino.write(str.encode('0'))
