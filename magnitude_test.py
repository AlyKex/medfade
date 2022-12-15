import fct_def
import matplotlib.pyplot as plt

readfile = fct_def.readfile("28_11_2022__14_27_35_laufen_30sec_simoin")
#28_11_2022__14_22_15_hinfallen_hinten_weiche_matte_simon
#28_11_2022__14_17_58_hinfallen_vorne_weiche_matte
#23_11_2022__10_54_27_gehen_normal
data_lin_sum_abs = []
data_calc_abs = []

detection_abs_low = []
detection_abs_high = []

detection_calc_abs = []
linelow = []
linehigh = []
linehigh_neg = []
bool = 1
pos_save = []
falldet = []

data_lin_x, data_lin_y, data_lin_z, data_lin_sum, data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum, data_orient_grad_x, data_orient_grad_y, data_orient_grad_z, data_et = fct_def.printfile(readfile)


data_lin_x_abs = [abs(val) for val in data_lin_x]
data_lin_y_abs = [abs(val) for val in data_lin_y]
data_lin_z_abs = [abs(val) for val in data_lin_z]

for i in range(len(data_lin_z_abs)-1):
    data_lin_sum_abs.append(data_lin_x_abs[i] +  data_lin_y_abs[i] + data_lin_z_abs[i])

for i in range(len(data_lin_sum_abs)):
    data_calc_abs.append(data_lin_sum_abs[i] - data_lin_sum_abs[i-5])


for i in range(len(data_lin_sum_abs)):
    detection_abs_high.append(0)
    detection_abs_low.append(0)

    linelow.append(2.7)
    linehigh.append(45)
    linehigh_neg.append(-45)

    if data_lin_sum_abs[i] <= 2.7:
        detection_abs_low[i] = 0.6

        if bool == 1:
            pos_save = i
            bool = 0

    if data_lin_sum_abs[i] >= 45:
        detection_abs_high[i] = 0.6

for i in range(len(data_lin_sum_abs)):
    if i < pos_save or i >= pos_save + 75:
        falldet.append(0)
    else:
        falldet.append(1)

for i in range(len(data_calc_abs)):
    detection_calc_abs.append(0)

    if data_calc_abs[i] >= 45:
        detection_calc_abs[i] = 1

    if data_calc_abs[i] <= -45:
        detection_calc_abs[i] = 1




plt.grid(axis = 'y')
plt.grid(axis = 'x')
plt.style.use("bmh")

#[550:650]

plt.subplot(2,1,1)
#plt.xlim([500, 650])

plt.title("Beschleunigungsverlauf")
plt.xlabel("Absolutwert der Beschleunigungen")
plt.ylabel("Beschleunigung in m/s^2")


plt.plot(data_lin_sum_abs, linewidth=1)
plt.plot(linelow, linewidth=1, color="red")
plt.plot(linehigh, linewidth=1, color="purple")

#plt.xlim(0,len(data_lin_sum_abs))

plt.legend(["Beschleunigungsverlauf","Unterer Threshold","Oberer Threshhold"])


plt.subplot(2,1,2)
#plt.xlim([500,650])

plt.xlabel("Detektierte Threshholds")
plt.ylabel("Threshold status")

plt.plot(detection_abs_high, linewidth=1, color="purple")
plt.plot(detection_abs_low, linewidth=1, color="red")
if sum(detection_abs_high) > 1:
    plt.plot(falldet)



plt.legend(["Oberer Threshold Status","Unterer Threshold Status","Erkannter Fall"])

plt.show()