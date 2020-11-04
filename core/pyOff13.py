import serial
import time
import os
import sys
import globalserial as gc

print("PIN 13 = LOW")
gc.arduino.write(str.encode('6'))