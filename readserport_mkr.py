import fct_def
import matplotlib.pyplot as plt

#acc_sum, vel_gyro, sensor_save = fct_def.readserport_mkr()
readfile = fct_def.readfile("26_01_2023__10_25_20_umfallen_hinten_1")
acc_sum = []
vel_gyro = []
lth = []
uth = []


'''''''''
fsave = input("file speichern?")
if "y" in fsave:
    fct_def.writefile(sensor_save)

print(acc_sum)
plt.subplot(2,1,1)
plt.plot(acc_sum)

print(vel_gyro)
plt.subplot(2,1,2)
plt.plot(vel_gyro)

plt.show()
'''''

acc_sum, vel_gyro = fct_def.print_mkr(readfile)

for i in range(len(acc_sum)):
    if acc_sum[i] <= 2.7:
        lth.append(1)

    else:
        lth.append(0)

    if acc_sum[i] >= 45:
        uth.append(1)

    else:
        uth.append(0)





plt.subplot(3,1,1)
plt.plot(acc_sum)


plt.subplot(3,1,2)
plt.plot(vel_gyro)

plt.subplot(3,1,3)
plt.plot(lth)
plt.plot(uth)



plt.show()

print(data)
exit()