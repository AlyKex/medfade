import os
import matplotlib.pyplot as plt
import fct_def

min_acc, max_acc, max_gvel = [], [], []

directory = 'Testaaunahmen_neu_neu\hinten_umfallen'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):

        readfile = fct_def.readfile(f)
        acc_sum, vel_gyro = fct_def.print_mkr(readfile)

        min_acc.append(min(acc_sum))
        max_acc.append(max(acc_sum))
        max_gvel.append((max(vel_gyro)))
        data = [min_acc]

fig = plt.figure(figsize=(10,7))


ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 2)
ax.grid()
bp = ax.boxplot(data)


plt.show()