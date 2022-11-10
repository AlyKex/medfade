# Importing Libraries
import serial
import matplotlib.pyplot as plt
import time
import fct_def
import numpy as np


#todo:
# --> Dantenerkennung
# tiefpass
# ableitungsfilter
# threshhold setzen
# -
# --> Datenteilung
# anderes keyword
# -
# --> Datenspeichern
# CSV?
# -
# --> Ablauf??
# einlesen bis serial port leer --> while
# dann daten verarbeiten, speichern, plotten, usw.
# wieder einlesen
# -
# datenauflösung bei arduino verändern / 100hz??
# samplerate bei plot ausgeben

sensvalstrip_save = []

data_lin_x ,data_lin_y, data_lin_z, data_lin_sum = [], [], [], []

data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum = [], [], [], []

data_orient_grad_x, data_orient_grad_y, data_orient_grad_z = [], [], []

data_ang_x, data_ang_y, data_ang_z = [], [], []

data_et = []
readfile = []

def readserport():

    while True:
        sensvalraw = ser.readline()
        sensvalstring = sensvalraw.decode()


        print(sensvalstring)
        if "abc" in sensvalstring:
            break

    start = time.time()
    for i in range(5*100*4):
        sensvalraw = ser.readline()
        sensvalstring = sensvalraw.decode()
        sensvalstrip = sensvalstring.strip()

        sensvalstrip_save.append(sensvalstrip)

        sensvalsplit = sensvalstrip.split()

        if "lb" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_x.append(float(sensvalsplit[0]))
            data_lin_y.append(float(sensvalsplit[1]))
            data_lin_z.append(float(sensvalsplit[2]))

            data_lin_sum.append(float(sensvalsplit[0])+float(sensvalsplit[1])+float(sensvalsplit[2]))


        elif "lk" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_kor_x.append(float(sensvalsplit[0]))
            data_lin_kor_y.append(float(sensvalsplit[1]))
            data_lin_kor_z.append(float(sensvalsplit[2]))
            data_lin_kor_sum.append(float(sensvalsplit[0])+float(sensvalsplit[1])+float(sensvalsplit[2]))


        elif "ow" in sensvalsplit:
            del sensvalsplit[0]
            data_orient_grad_x.append(float(sensvalsplit[0]))
            data_orient_grad_y.append(float(sensvalsplit[1]))
            data_orient_grad_z.append(float(sensvalsplit[2]))
        elif "et" in sensvalsplit:
            data_et.append(float(sensvalsplit[1]))
            break

    return start




ser = serial.Serial(port='COM4', baudrate=2000000, timeout=2)

start = readserport()
end = time.time()
ser.close()

fct_def.writefile(sensvalstrip_save)

ylim_data_lin = sorted(data_lin_sum)
plt.style.use("ggplot")
plt.subplot(3,1,1)
plt.ylim(ylim_data_lin[0] * 1.1, max(data_lin_sum)*1.1)
plt.plot(data_lin_x,linewidth=1)
plt.plot(data_lin_y,linewidth=1)
plt.plot(data_lin_z,linewidth=1)
plt.plot(data_lin_sum,linewidth=1)


ylim_data_lin_kor = sorted(data_lin_kor_sum)
plt.subplot(3,1,2)
plt.ylim(ylim_data_lin_kor[0]*1.1, max(data_lin_kor_sum)*1.1)
plt.plot(data_lin_kor_x,linewidth=1)
plt.plot(data_lin_kor_y,linewidth=1)
plt.plot(data_lin_kor_z,linewidth=1)
plt.plot(data_lin_kor_sum,linewidth=1)

plt.subplot(3,1,3)
plt.ylim(0,360)
plt.plot(data_orient_grad_x,linewidth=1)


plt.show()

readfile = fct_def.readfile()

print(readfile)
print(end - start)
print(data_et)
