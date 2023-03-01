import fct_def
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import csv
import os

directory = 'Testaufnahmen_Neu'



acc_sum = []
vel_gyro = []

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

acc_sum, vel_gyro = fct_def.print_mkr(readfile)

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


plt.subplot(3,1,1)
plt.plot(acc_sum, linewidth = 0.5)

plt.subplot(3,1,2)
plt.plot(vel_gyro, linewidth = 0.5)

plt.subplot(3,1,3)
plt.plot(lth, linewidth = 0.5)
plt.plot(uth, linewidth = 0.5)
plt.plot(ugv, linewidth = 0.5)


if sum(uth_last) > 0:
    if min(uth_last) - max(lth_last) <= 25:
        if min(ugv_last) - max(lth_last) <= 25:
            print("ein fall wurde erkannt")
            fb = [min(uth_last) - 100, min(uth_last) + 100]


print("Summe der Samples im LTH Bereich")
print((sum(lth)))
print("Summe der Samples im UTH Bereich")
print(sum(uth))
print("Letzer Sample im LTH Bereich")
print(max(lth_last))
print("Erster Sample im UTH Bereich")
print(min(uth_last))
print("Erster Sample im UGV Bereich")
print(min(ugv_last))
print("Maximale Beschleunigung im Sample")
print(max(acc_sum))
print("Minimale Beschleunigung im Sample")
print(min(acc_sum))
print("Erster Fallbereich")
print(min(lth_last))
print("Letzter Fallbereich")
print(max(uth_last))
print("Fallbereich")
print(fb)


file_path.strip()

file_path = os.path.basename(os.path.normpath(file_path))


plt.show()

exit()
