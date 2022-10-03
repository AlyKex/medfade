# Importing Libraries
import serial
import matplotlib.pyplot as plt
import time
import sys


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




def readserport():

    for i in range(1000*4):

        sensvalraw = ser.readline()

        sensvalstring = sensvalraw.decode()

        sensvalstrip = sensvalstring.strip()

        sensvalsplit = sensvalstring.split()


        if "lb" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_x.append(float(sensvalsplit[0]))
            data_lin_y.append(float(sensvalsplit[1]))
            data_lin_z.append(float(sensvalsplit[2]))


        if "lk" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_kor_x.append(float(sensvalsplit[0]))
            data_lin_kor_y.append(float(sensvalsplit[1]))
            data_lin_kor_z.append(float(sensvalsplit[2]))

        if "wb" in sensvalsplit:
            del sensvalsplit[0]
            data_ang_x.append(float(sensvalsplit[0]))
            data_ang_y.append(float(sensvalsplit[1]))
            data_ang_z.append(float(sensvalsplit[2]))

        if "ow" in sensvalsplit:
            del sensvalsplit[0]
            data_orient_grad_x.append(float(sensvalsplit[0]))
            data_orient_grad_y.append(float(sensvalsplit[1]))
            data_orient_grad_z.append(float(sensvalsplit[2]))







data_lin_x = []
data_lin_y = []
data_lin_z = []

data_lin_kor_x = []
data_lin_kor_y = []
data_lin_kor_z = []

data_orient_grad_x = []
data_orient_grad_y = []
data_orient_grad_z = []

data_ang_x = []
data_ang_y = []
data_ang_z = []







ser = serial.Serial(port='COM4', baudrate=2000000, timeout=2)

sensvalraw = ser.readline()

start = time.time()

readserport()

end = time.time()

print(data_lin_x)
print(data_lin_y)
print(data_lin_z)

ser.close()



plt.figure()
plt.subplot(311)
plt.ylim(-15, 15)
plt.plot(data_lin_kor_x)

plt.subplot(312)
plt.ylim(-15, 15)
plt.plot(data_lin_kor_y)

plt.subplot(313)
plt.ylim(-15, 15)
plt.plot(data_lin_kor_z)

print(end - start)



plt.show()
