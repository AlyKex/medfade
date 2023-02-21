import fct_def
import matplotlib.pyplot as plt




acc_sum, vel_gyro, sensor_save = fct_def.readserport_mkr()


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
