import serial
import time
import os
import sys
import globalserial as gc
print("PIN 2 = HIGH")
gc.arduino.write(str.encode('5'))