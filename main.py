# Importing Libraries
import serial
import matplotlib.pyplot as plt
import time
import sys


def readserport():

    for i in range(1):

        sensvalraw = ser.readline()
        bin_test.append(sensvalraw)

        sensvalstring = sensvalraw.decode()
        bin_test1.append(sensvalstring)

        sensvalstrip = sensvalstring.strip()
        bin_test2.append(sensvalstrip)

        sensvalsplit = sensvalstring.split()
        bin_test3.append(sensvalsplit)

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







data_lin_x = []
data_lin_y = []
data_lin_z = []

data_lin_kor_x = []
data_lin_kor_y = []
data_lin_kor_z = []

bin_test = []
bin_test1 = []
bin_test2 = []
bin_test3 = []



ser = serial.Serial(port='COM3', baudrate=2000000, timeout=2)

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



#plt.show()


print(end - start)
print(bin_test)
print(sys.getsizeof(bin_test))

print(bin_test1)
print(bin_test2)
print(bin_test3)