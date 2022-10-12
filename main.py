# Importing Libraries
import serial
import matplotlib.pyplot as plt
import time
import fct_def


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

sensvalstrip_save = []

data_lin_x ,data_lin_y, data_lin_z, data_lin_sum = [], [], [], []

data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum = [], [], [], []

data_orient_grad_x, data_orient_grad_y, data_orient_grad_z = [], [], []

data_ang_x, data_ang_y, data_ang_z = [], [], []

def readserport():
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


        if "lk" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_kor_x.append(float(sensvalsplit[0]))
            data_lin_kor_y.append(float(sensvalsplit[1]))
            data_lin_kor_z.append(float(sensvalsplit[2]))
            data_lin_kor_sum.append(float(sensvalsplit[0])+float(sensvalsplit[1])+float(sensvalsplit[2]))


        if "ow" in sensvalsplit:
            del sensvalsplit[0]
            data_orient_grad_x.append(float(sensvalsplit[0]))
            data_orient_grad_y.append(float(sensvalsplit[1]))
            data_orient_grad_z.append(float(sensvalsplit[2]))





ser = serial.Serial(port='COM4', baudrate=2000000, timeout=2)

ser.readline()

start = time.time()
readserport()
end = time.time()
ser.close()

fct_def.writefile(sensvalstrip_save)

ylim_data_lin = sorted(data_lin_sum)
plt.subplot(3,1,1)
plt.ylim(ylim_data_lin[0] * 1.1, max(data_lin_sum)*1.1)
plt.plot(data_lin_x)
plt.plot(data_lin_y)
plt.plot(data_lin_z)
plt.plot(data_lin_sum)


ylim_data_lin_kor = sorted(data_lin_kor_sum)
plt.subplot(3,1,2)
plt.ylim(ylim_data_lin_kor[0]*1.1, max(data_lin_kor_sum)*1.1)
plt.plot(data_lin_kor_x)
plt.plot(data_lin_kor_y)
plt.plot(data_lin_kor_z)
plt.plot(data_lin_kor_sum)

plt.subplot(3,1,3)
plt.ylim(0,360)
plt.plot(data_orient_grad_x)

plt.show()

print(end - start)
