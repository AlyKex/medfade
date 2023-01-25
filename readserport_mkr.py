import fct_def
import matplotlib.pyplot as plt

acc_sum, vel_gyro, sensor_save = fct_def.readserport_mkr()
fct_def.writefile(sensor_save)

print(acc_sum)
plt.subplot(2,1,1)
plt.plot(acc_sum)

print(vel_gyro)
plt.subplot(2,1,2)
plt.plot(vel_gyro)

plt.show()
exit()