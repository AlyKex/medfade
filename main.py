# Importing Libraries
import serial
import matplotlib.pyplot as plt
import time


def readserport():
    datasave1 = []
    datasave2 = []
    datasave3 = []

    while len(data_lin_z) < 10:
        sensvalraw = ser.readline()

        sensvalstring = sensvalraw.decode()


        sensvalsplit = sensvalstring.split(';')

        if "lb" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_x.append(float(sensvalsplit[0]))
            data_lin_y.append(float(sensvalsplit[1]))
            data_lin_z.append(float(sensvalsplit[2]))


        elif "lk" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_kor_x.append(float(sensvalsplit[0]))
            data_lin_kor_y.append(float(sensvalsplit[1]))
            data_lin_kor_z.append(float(sensvalsplit[2]))





data_lin_x = []
data_lin_y = []
data_lin_z = []

data_lin_kor_x = []
data_lin_kor_y = []
data_lin_kor_z = []

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
plt.subplot(211)
plt.ylim(0, 15)
plt.plot(data_lin_z)

plt.subplot(212)
plt.ylim(-15, 15)
plt.plot(data_lin_kor_z)



plt.show()


print(end - start)