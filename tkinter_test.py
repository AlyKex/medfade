import fct_def
import csv
import os

directory = 'Testaufnahmen_Neu'

# open the file in the write mode
with open('medfades_Data.txt', mode='w', newline='') as f:

    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(["Name;" "Max Acc;" "A. Samples in UTH;" "erster UTH;" "letzter UTH;" "Min Acc;" "A. Samples in LTH;" "erster LTH;" "letzter LTH;" "Max GyVel;" "A. Samples in UGV;" "erster UGV;" "letzter UGV;" "Fall;" "Fallbereich;" "Fallbereich;"])

    for filename in os.listdir(directory):

        acc_sum = []
        vel_gyro = []
        lth = [0]
        uth = [0]
        ugv = [0]

        lth_last = []
        uth_last = []
        ugv_last = []

        fall = 0
        fb = [0, 0]

        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):

            readfile = fct_def.readfile(f)
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
                if vel_gyro[i] <= 300:
                    ugv.append(0)
                else:
                    ugv.append(1)
                    ugv_last.append(i)

            f.strip()
            f = os.path.basename(os.path.normpath(f))

            if sum(uth_last) == 0:
                uth_last.append(0)

            if sum(lth_last) == 0:
                lth_last.append(0)

            if sum(ugv_last) == 0:
                ugv_last.append(0)

            if sum(uth_last) > 0:
                if min(uth_last) - max(lth_last) <= 25:
                    if min(ugv_last) - max(lth_last) <= 25:
                        print("ein fall wurde erkannt")
                        fall = 1
                        fb = [min(uth_last) - 100, min(uth_last) + 100]

            csv_file_data = f'{f}; {max(acc_sum)}; {sum(uth)}; {min(uth_last)}; {max(uth_last)}; {min(acc_sum)}; {sum(lth)}; {min(lth_last)}; {max(lth_last)}; {max(vel_gyro)}; {sum(ugv)}; {min(ugv_last)}; {max(ugv_last)}; {fall}; {fb[0]}; {fb[1]}; '
            writer.writerow([csv_file_data])



exit()
