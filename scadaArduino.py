from tkinter import *
import tkinter.font as tkFont
import os
import time
import subprocess
import serial
import threading
from tkinter import messagebox
import core.globalserial as gc

# VARIABLES GLOBAL IMPORTANTE
debug_mode = False

# Funciones
def on_closing():
    if( debug_mode ):
        print("called: on_closing")

    global appForm
    global pushButtonProcess
    if messagebox.askokcancel("Salir", "¿Estas seguro de querer salir?"):
        pushButtonProcess.kill()
        appForm.destroy()

def activatePin(num_pin):
    if( debug_mode ):
        print("called: activePin("+str(num_pin)+")")

    os.system("sudo core/arduinoOn"+str(num_pin)+".sh &")
    updateForm()

def disablePin(num_pin):
    if( debug_mode ):
        print("called: disablePin("+str(num_pin)+")")

    os.system("sudo core/arduinoOff"+str(num_pin)+".sh &")
    updateForm()

def updateForm():
    global pushButtonState

    filePin13 = open("core/state_arduino_pin13.txt", "r")
    filePin2 = open("core/state_arduino_pin2.txt", "r")
    filePin7 = open("core/state_arduino_pin7.txt", "r")

    # PIN 13 (LED ROJA).
    for line in filePin13:
        field = line.split("\n")
        statePin = field[0]
        #print("Monitoreo de Push ha detectado valor: ", field1)
        if int(statePin) == 1:
            buttonState13['image'] = imageOn
            buttonOn13['state'] = 'disabled'
            buttonOff13['state'] = 'active'
        else:
            buttonState13['image'] = imageOff
            buttonOn13['state'] = 'active'
            buttonOff13['state'] = 'disable'
    filePin13.close()
    
    # PIN 2 (LED AZUL).
    for line in filePin2:
        field = line.split("\n")
        statePin = field[0]
        #print("Monitoreo de Push ha detectado valor: ", field1)
        if int(statePin) == 1:
            buttonState2['image'] = imageOn
            buttonOn2['state'] = 'disabled'
            buttonOff2['state'] = 'active'

        else:
            buttonState2['image'] = imageOff
            buttonOn2['state'] = 'active'
            buttonOff2['state'] = 'disable'
    
    filePin2.close()

    for line in filePin7:
        field = line.split("\n")
        statePin = field[0]
        print("xass: ", statePin)
        #print("Monitoreo de Push ha detectado valor: ", field1)
        if int(statePin) == 1:
            print("xass222")
            pushButtonState['image'] = imageOn
        else:
            print("xas3333")
            pushButtonState['image'] = imageOff

    filePin7.close()
    appForm.after(1000, updateForm)

# Diseño de formulario
appForm = Tk()
appForm.title('Scada Arduino')
appForm.geometry('1024x600+0+0')

imageOn = PhotoImage(file='on.png')
imageOff = PhotoImage(file='off.png')

labelTitle = Label(appForm, text="Scada Python App", font="none 24 bold")
labelTitle.grid(row=0, column=5)

# Salida 13
labelPort13 = Label(appForm, text="Salida #13")
buttonState13 = Button(appForm, image=imageOff)
buttonOn13  = Button(appForm, text="Encender", command= lambda: activatePin(13))
buttonOff13  = Button(appForm, text="Apagar",  command= lambda: disablePin(13))
labelPort13.grid(row=1, column=5)
buttonState13.grid(row=2, column=5)
buttonOn13.grid(row=3, column=5)
buttonOff13.grid(row=4, column=5)

# Salida 2
labelPort2 = Label(appForm, text="Salida #2")
buttonState2 = Button(appForm, image=imageOff)
buttonOn2  = Button(appForm, text="Encender", command= lambda: activatePin(2))
buttonOff2  = Button(appForm, text="Apagar", command= lambda: disablePin(2))
labelPort2.grid(row=1, column=6)
buttonState2.grid(row=2, column=6)
buttonOn2.grid(row=3, column=6)
buttonOff2.grid(row=4, column=6)

# Salida 8
labelPort8 = Label(appForm, text="Salida #8")
buttonState8 = Button(appForm, image=imageOff)
buttonOn8  = Button(appForm, text="Encender", command= lambda: activatePin(8))
buttonOff8  = Button(appForm, text="Apagar", command= lambda: disablePin(8))
labelPort8.grid(row=1, column=7)
buttonState8.grid(row=2, column=7)
buttonOn8.grid(row=3, column=7)
buttonOff8.grid(row=4, column=7)

# Pulsador (Salida 7)
pushLabel7 = Label(appForm, text="Salida #7 (Monitoreo Pulsador)")
pushButtonState = Button(appForm, image=imageOff)
pushLabel7.grid(row=1, column=8)
pushButtonState.grid(row=2, column=8)

pushButtonProcess = subprocess.Popen(['python3', 'core/pyPush.py'])
disablePin(13)
disablePin(2)

updateForm()

appForm.protocol("WM_DELETE_WINDOW", on_closing)
appForm.mainloop()