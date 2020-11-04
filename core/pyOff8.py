import serial
import time
import os
import sys
import globalserial as gc
print("PIN 8 = LOW")
gc.arduino.write(str.encode('8'))