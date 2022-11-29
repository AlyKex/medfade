import fct_def
import matplotlib.pyplot as plt
import numpy as np

readfile = fct_def.readfile("28_11_2022__14_22_15_hinfallen_hinten_weiche_matte_simon")




data_lin_x, data_lin_y, data_lin_z, data_lin_sum, data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum, data_orient_grad_x, data_orient_grad_y, data_orient_grad_z, data_et = fct_def.printfile(readfile)


ylim_data_lin = sorted(data_lin_sum)
plt.style.use("ggplot")
plt.subplot(3,1,1)
plt.ylim(ylim_data_lin[0] * 1.1, max(data_lin_sum)*1.1)
#plt.plot(data_lin_x,linewidth=1)
#plt.plot(data_lin_y,linewidth=1)
#plt.plot(data_lin_z,linewidth=1)
plt.plot(data_lin_sum,linewidth=1)


ylim_data_lin_kor = sorted(data_lin_kor_sum)
plt.subplot(3,1,2)
plt.ylim(ylim_data_lin_kor[0]*1.1, max(data_lin_kor_sum)*1.1)
#plt.plot(data_lin_kor_x,linewidth=1)
#plt.plot(data_lin_kor_y,linewidth=1)
#plt.plot(data_lin_kor_z,linewidth=1)
plt.plot(data_lin_kor_sum,linewidth=1)

plt.subplot(3,1,3)
plt.ylim(-360,360)
plt.plot(data_orient_grad_x, linewidth=1)
plt.plot(data_orient_grad_y, linewidth=1)
plt.plot(data_orient_grad_z, linewidth=1)

plt.show()
