import serial
import time
import os
import sys
import globalserial as gc

print("PIN 12 = LOW")
gc.arduino.write(str.encode('2'))