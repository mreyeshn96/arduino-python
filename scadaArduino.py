from tkinter import *
import tkinter.font as tkFont
import os
import time
import subprocess
import serial
import threading
from tkinter import messagebox
import core.globalserial as gc
import core.globalvars as gv

# VARIABLES GLOBAL IMPORTANTE
debug_mode = False
state_fantastic = False
os.system("sudo chmod -R 777 ./*")

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
    #global pushButtonState

    filePin13 = open("core/state_arduino_pin13.txt", "r")
    filePin2 = open("core/state_arduino_pin2.txt", "r")
    filePin8 = open("core/state_arduino_pin8.txt", "r")
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

    for line in filePin8:
        field = line.split("\n")
        statePin = field[0]
        #print("Monitoreo de Push ha detectado valor: ", field1)
        if int(statePin) == 1:
            buttonState8['image'] = imageOn
            buttonOn8['state'] = 'disabled'
            buttonOff8['state'] = 'active'

        else:
            buttonState8['image'] = imageOff
            buttonOn8['state'] = 'active'
            buttonOff8['state'] = 'disable'
    
    filePin8.close()

    for line in filePin7:
        field = line.split("\n")
        statePin = field[0]
        #print("Monitoreo de Push ha detectado valor: ", field1)
        if int(statePin) == 1:
            pass
            #pushButtonState['image'] = imageOn
        else:
            pass
            #pushButtonState['image'] = imageOff

    filePin7.close()
    appForm.after(1000, updateForm)

def openCronForm(num_pin):

    gv.CURRENT_CRON_PIN = num_pin

    appCronForm = Toplevel(appForm)
    appCronForm.title('Cron Form')
    appCronForm.geometry('1024x600+0+0')

    Label(appCronForm, text='Programar Cron para Salida {0}'.format(gv.CURRENT_CRON_PIN)).grid(row=0, column=1)
    Label(appCronForm, text='Hora inicial (HI):').grid(row=5,column=0)
    Label(appCronForm, text='Minuto inicial (MI):').grid(row=6,column=0)
    Label(appCronForm, text='Hora final (HF):').grid(row=7,column=0)
    Label(appCronForm, text='Minuto final (MF):').grid(row=8,column=0)

    entryHI = Entry(appCronForm)
    entryMI = Entry(appCronForm)
    entryHF = Entry(appCronForm)
    entryMF = Entry(appCronForm)

    entryHI.grid(row=5,column=1)
    entryMI.grid(row=6,column=1)
    entryHF.grid(row=7,column=1)
    entryMF.grid(row=8,column=1)

    actionCron = Button(appCronForm, text='Guardar', command=lambda: createCron(num_pin, entryHI.get(), entryMI.get(), entryHF.get(), entryMF.get()))
    actionCron.grid(row=9,column=0)

    #currentTime = time.strftime("%H:%M:%S")
    #Label(appCronForm, text=" - - Tiempo - - ").grid(row=10,column=1)
    #labelTime = Label(appCronForm, text=currentTime).grid(row=11,column=1)

def createCron(pin, hourI, minI, hourF, minF):
    if pin < 1000:
        fileBashOn = 'arduinoOn{0}.sh'.format(pin)
        fileBashOff = 'arduinoOff{0}.sh'.format(pin)
        fileCronStart = 'tarea{0}Start'.format(pin)
        fileCronEnd = 'tarea{0}End'.format(pin)

        cronStringOn = '{0} {1} * * * root /home/reyes/Documentos/GitHub/arduino-python/core/{2}'.format(minI, hourI, fileBashOn)
        cronStringOff = '{0} {1} * * * root /home/reyes/Documentos/GitHub/arduino-python/core/{2}'.format(minF, hourF, fileBashOff)

        print(cronStringOn)
        print(cronStringOff)

        cronTask = open(r"/etc/cron.d/{0}".format(fileCronStart), 'w+')
        cronTask.write(cronStringOn)
        cronTask.write('\n')
        cronTask.close()
        os.system('sudo chmod -R 777 /etc/cron.d/{0}'.format(fileCronStart))

        cronTask = open(r"/etc/cron.d/{0}".format(fileCronEnd), 'w+')
        cronTask.write(cronStringOff)
        cronTask.write('\n')
        cronTask.close()
        os.system('sudo chmod -R 777 /etc/cron.d/{0}'.format(fileCronEnd))

        os.system('sudo chmod -R 755 /etc/cron.d/{0}'.format(fileCronStart))
        os.system('sudo chmod -R 755 /etc/cron.d/{0}'.format(fileCronEnd))

        os.system('sudo /etc/init.d/cron restart &')
    elif pin == 1000:
        createFantastic(pin, hourI, minI, hourF, minF)

def createFantastic(pin, hourI, minI, hourF, minF):
    fileBashOn = 'arduinoFantasticOn.sh'
    fileBashOff = 'arduinoFantasticOff.sh'
    fileCronStart = 'tareaFanStart'
    fileCronEnd = 'tareaFanEnd'

    cronStringOn = '{0} {1} * * * root /home/reyes/Documentos/GitHub/arduino-python/core/{2}'.format(minI, hourI, fileBashOn)
    cronStringOff = '{0} {1} * * * root /home/reyes/Documentos/GitHub/arduino-python/core/{2}'.format(minF, hourF, fileBashOff)

    print(cronStringOn)
    print(cronStringOff)

    cronTask = open(r"/etc/cron.d/{0}".format(fileCronStart), 'w+')
    cronTask.write(cronStringOn)
    cronTask.write('\n')
    cronTask.close()
    os.system('sudo chmod -R 777 /etc/cron.d/{0}'.format(fileCronStart))

    cronTask = open(r"/etc/cron.d/{0}".format(fileCronEnd), 'w+')
    cronTask.write(cronStringOff)
    cronTask.write('\n')
    cronTask.close()
    os.system('sudo chmod -R 777 /etc/cron.d/{0}'.format(fileCronEnd))

    os.system('sudo chmod -R 755 /etc/cron.d/{0}'.format(fileCronStart))
    os.system('sudo chmod -R 755 /etc/cron.d/{0}'.format(fileCronEnd))

    os.system('sudo /etc/init.d/cron restart &')


def reloj():
    pass

def alternateFantastic():
    global state_fantastic
    if state_fantastic:
        os.system("sudo core/arduinoFantasticOn.sh &")
    else:
        os.system("sudo core/arduinoFantasticOff.sh &")
    state_fantastic = not state_fantastic
# Diseño de formulario
appForm = Tk()
appForm.title('Scada Arduino')
appForm.geometry('1024x600+0+0')

imageOn = PhotoImage(file='on.png')
imageOff = PhotoImage(file='off.png')

labelTitle = Label(appForm, text="Scada Python App", font="none 24 bold")
labelTitle.grid(row=0, column=5, columnspan=2)

# Salida 13
labelPort13 = Label(appForm, text="Salida #13")
buttonState13 = Button(appForm, image=imageOff)
buttonOn13  = Button(appForm, text="Encender", command= lambda: activatePin(13))
buttonOff13  = Button(appForm, text="Apagar",  command= lambda: disablePin(13))
labelPort13.grid(row=1, column=5)
buttonState13.grid(row=2, column=5)
buttonOn13.grid(row=3, column=5)
buttonOff13.grid(row=4, column=5)
buttonCron13 = Button(appForm, text='Programar', command= lambda: openCronForm(13))
buttonCron13.grid(row=5, column=5)

# Salida 2
labelPort2 = Label(appForm, text="Salida #2")
buttonState2 = Button(appForm, image=imageOff)
buttonCron2 = Button(appForm, text='Programar', command= lambda: openCronForm(2))
buttonOn2  = Button(appForm, text="Encender", command= lambda: activatePin(2))
buttonOff2  = Button(appForm, text="Apagar", command= lambda: disablePin(2))
labelPort2.grid(row=1, column=6)
buttonState2.grid(row=2, column=6)
buttonOn2.grid(row=3, column=6)
buttonOff2.grid(row=4, column=6)
buttonCron2.grid(row=5, column=6)

# Salida 8
labelPort8 = Label(appForm, text="Salida #8")
buttonState8 = Button(appForm, image=imageOff)
buttonOn8  = Button(appForm, text="Encender", command= lambda: activatePin(8))
buttonOff8  = Button(appForm, text="Apagar", command= lambda: disablePin(8))
labelPort8.grid(row=1, column=15)
buttonState8.grid(row=2, column=15)
buttonOn8.grid(row=3, column=15)
buttonOff8.grid(row=4, column=15)
buttonCron8 = Button(appForm, text='Programar', command= lambda: openCronForm(8))
buttonCron8.grid(row=5, column=15)

# Salida 12
labelPort12 = Label(appForm, text="Salida #12")
buttonState12 = Button(appForm, image=imageOff)
buttonOn12  = Button(appForm, text="Encender", command= lambda: activatePin(12))
buttonOff12  = Button(appForm, text="Apagar", command= lambda: disablePin(12))
labelPort12.grid(row=1, column=16)
buttonState12.grid(row=2, column=16)
buttonOn12.grid(row=3, column=16)
buttonOff12.grid(row=4, column=16)
buttonCron12 = Button(appForm, text='Programar', command= lambda: openCronForm(12))
buttonCron12.grid(row=5, column=16)

# Pulsador (Salida 7)
#pushLabel7 = Label(appForm, text="Salida #7 (Monitoreo Pulsador)")
#pushButtonState = Button(appForm, image=imageOff)
#pushLabel7.grid(row=1, column=20)
#pushButtonState.grid(row=2, column=20)

fantasticButtonCron = Button(appForm, text="Programar luces", command=lambda: openCronForm(1000))
fantasticButtonCron.grid(row=20, column=1)
fantasticButton = Button(appForm, text="Encender luces fantasticas", command=lambda: alternateFantastic())
fantasticButton.grid(row=21, column=1)

pushButtonProcess = subprocess.Popen(['python3', 'core/pyPush.py'])
#disablePin(13)
#disablePin(2)

updateForm()

appForm.protocol("WM_DELETE_WINDOW", on_closing)
appForm.mainloop()