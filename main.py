# Importing Libraries
import serial
import matplotlib.pyplot as plt
import time


def readserport():
    datasave1 = []
    datasave2 = []
    datasave3 = []

    while len(datasave1) < 100:
        sensvalraw = ser.readline()

        sensvalstring = sensvalraw.decode()

        sensvalsplit = sensvalstring.split(';')

        datasave1.append(float(sensvalsplit[0]))
        datasave2.append(float(sensvalsplit[1]))
        datasave3.append(float(sensvalsplit[2]))

    return [datasave1, datasave2, datasave3]

data_lin_x = []
data_lin_y = []
data_lin_z = []

data_lin_kor_x = []
data_lin_kor_y = []
data_lin_kor_z = []

ser = serial.Serial(port='COM3', baudrate=2000000, timeout=2)

sensvalraw = ser.readline()

start = time.time()

[data_lin_x, data_lin_y, data_lin_z] = readserport()

end = time.time()

print(data_lin_x)
print(data_lin_y)
print(data_lin_z)

ser.close()



plt.figure()
plt.subplot(211)
plt.ylim(0, 15)
plt.plot(data_lin_z)

#plt.subplot(212)
#plt.ylim(-15, 15)
#plt.plot(data_lin_kor_z)



plt.show()


print(end - start)