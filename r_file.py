import fct_def
import matplotlib.pyplot as plt

acc_sum = []
vel_gyro = []
lth = []
uth = []
ugv = []

lth_last = 0
uth_last = []
ugv_last = []


fname = "26_01_2023__10_53_33_zusammensacken_2_herzinfarkt"

readfile = fct_def.readfile(fname)



'''

print(acc_sum)
plt.subplot(2,1,1)
plt.plot(acc_sum)

print(vel_gyro)
plt.subplot(2,1,2)
plt.plot(vel_gyro)

plt.show()

fsave = input("file speichern?")
if "y" in fsave:
    fct_def.writefile(sensor_save)

'''
acc_sum, vel_gyro = fct_def.print_mkr(readfile)

for i in range(len(acc_sum)):
    if acc_sum[i] <= 1.8:
        lth.append(1)
        lth_last = i

    else:
        lth.append(0)

    if acc_sum[i] >= 45:
        uth.append(1)
        uth_last.append(i)

    else:
        uth.append(0)

for i in range(len(vel_gyro)):
    if vel_gyro[i] <=300:
        ugv.append(0)
    else:
        ugv.append(1)
        ugv_last.append(i)


plt.subplot(3,1,1)

plt.plot(acc_sum, linewidth = 0.5)


plt.subplot(3,1,2)
plt.plot(vel_gyro, linewidth = 0.5)


plt.subplot(3,1,3)

plt.plot(lth, linewidth = 0.5)
plt.plot(uth, linewidth = 0.5)
plt.plot(ugv, linewidth = 0.5)

print(lth_last)
if sum(uth_last) > 0:
    print(min(uth_last))
    print(min(ugv_last))
if sum(uth_last) > 0:
    if min(uth_last) - lth_last <= 25:
        if min(ugv_last) - lth_last <= 50:
            print("ein fall wurde erkannt")


print((sum(lth)))
print(max(acc_sum))
print(min(acc_sum))
print(max(acc_sum)/min(acc_sum))

plt.show()

exit()
