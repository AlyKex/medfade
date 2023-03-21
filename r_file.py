import fct_def
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os




acc_sum = []
vel_gyro = []
heading = []
roll = []
pitch = []

lth = []
uth = []
ugv = []

fb = []

lth_last = []
uth_last = []
ugv_last = []


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

readfile = fct_def.readfile(file_path)

acc_sum, vel_gyro, heading, roll, pitch= fct_def.print_mkr_mega(readfile)

for i in range(len(acc_sum)):
    if acc_sum[i] <= 2.5:
        lth.append(1)
        lth_last.append(i)


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


plt.subplot(5,1,1)
plt.plot(acc_sum, linewidth = 0.5)

plt.subplot(5,1,2)
plt.plot(vel_gyro, linewidth = 0.5)

plt.subplot(5,1,3)
plt.plot(heading, linewidth = 0.5)

plt.subplot(5,1,4)
plt.plot(roll, linewidth = 0.5)

plt.subplot(5,1,5)
plt.plot(pitch, linewidth = 0.5)

plt.show()

file_path.strip()

file_path = os.path.basename(os.path.normpath(file_path))
exit()
