from tkinter import *
import tkinter.font as tkFont
import os
import time
import subprocess
import serial
import threading
from tkinter import messagebox
import core.globalserial as gc

# EXTRA
os.system('chmod -R 777 ./*')

# Funciones
def on_closing():
    global appForm
    if messagebox.askokcancel("Salir", "¿Estas seguro de querer salir?"):
        appForm.destroy()

def activatePin():
    os.system("sudo core/arduino_examen_on.sh &")
    updateForm()

def disablePin():
    os.system("sudo core/arduino_examen_off.sh &")
    updateForm()

def updateForm():
    filePin = open("core/state_arduino_examen.txt", "r")
    #filePinOff = open("core/state_arduino_actionOff.txt", "r")

    # PIN 13 (LED ROJA).
    for line in filePin:
        field = line.split("\n")
        statePin = field[0]
        #print("Monitoreo de Push ha detectado valor: ", field1)
        if int(statePin) == 1:
            buttonStateOnPin8['image'] = imageOff
            buttonStateOnPin4['image'] = imageOn
            buttonStateOnPin2['image'] = imageOn
            buttonStateOffPin8['image'] = imageOff
            buttonStateOffPin4['image'] = imageOff
            buttonStateOffPin2['image'] = imageOff

            buttonActionOn['state'] = 'disabled'
            buttonActionOff['state'] = 'active'
        else:
            buttonStateOffPin8['image'] = imageOn
            buttonStateOffPin4['image'] = imageOn
            buttonStateOffPin2['image'] = imageOff
            buttonStateOnPin8['image'] = imageOff
            buttonStateOnPin4['image'] = imageOff
            buttonStateOnPin2['image'] = imageOff

            buttonActionOn['state'] = 'active'
            buttonActionOff['state'] = 'disabled'

    filePin.close()

    appForm.after(1000, updateForm)

# Diseño de formulario
appForm = Tk()
appForm.title('Scada Arduino')
appForm.geometry('1024x600+0+0')

imageOn = PhotoImage(file='on.png')
imageOff = PhotoImage(file='off.png')

labelTitle = Label(appForm, text="Scada Python App", font="none 24 bold")
labelTitle.grid(row=0, column=5)

buttonActionOn = Button(appForm, text="Encender", command= activatePin)
buttonActionOff = Button(appForm, text="Apagar", command= disablePin)
buttonStateOnPin8 = Button(appForm, image=imageOff)
buttonStateOnPin4 = Button(appForm, image=imageOff)
buttonStateOnPin2 = Button(appForm, image=imageOff)
buttonStateOffPin8 = Button(appForm, image=imageOff)
buttonStateOffPin4 = Button(appForm, image=imageOff)
buttonStateOffPin2 = Button(appForm, image=imageOff)

buttonActionOn.grid(row=1, column=0)
buttonActionOff.grid(row=2, column=0)
buttonStateOnPin8.grid(row=1, column=2)
buttonStateOnPin4.grid(row=1, column=3)
buttonStateOnPin2.grid(row=1, column=4)
buttonStateOffPin8.grid(row=2, column=2)
buttonStateOffPin4.grid(row=2, column=3)
buttonStateOffPin2.grid(row=2, column=4)

activatePin()
updateForm()

appForm.protocol("WM_DELETE_WINDOW", on_closing)
appForm.mainloop()