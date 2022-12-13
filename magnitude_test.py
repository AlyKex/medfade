import fct_def
import matplotlib.pyplot as plt

readfile = fct_def.readfile("28_11_2022__14_22_15_hinfallen_hinten_weiche_matte_simon")


data_lin_sum_abs = []

data_lin_x, data_lin_y, data_lin_z, data_lin_sum, data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum, data_orient_grad_x, data_orient_grad_y, data_orient_grad_z, data_et = fct_def.printfile(readfile)


data_lin_x_abs = [abs(val) for val in data_lin_kor_x]
data_lin_y_abs = [abs(val) for val in data_lin_kor_y]
data_lin_z_abs = [abs(val) for val in data_lin_kor_z]

for i in range(len(data_lin_z_abs)-1):
    data_lin_sum_abs.append(data_lin_x_abs[i] +  data_lin_y_abs[i] + data_lin_z_abs[i])


plt.style.use("ggplot")
plt.subplot(3,1,1)
plt.plot(data_lin_kor_sum,linewidth=1)

plt.subplot(3,1,2)
plt.plot(data_lin_sum_abs,linewidth=1)

plt.subplot(3,1,3)
plt.xticks(range(0,100))
plt.plot(data_lin_sum_abs[550:650],linewidth=1)


plt.show()


