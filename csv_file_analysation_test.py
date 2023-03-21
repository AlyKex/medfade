import fct_def
import csv
import os

acc_sum = []
vel_gyro = []
heading = []
roll = []
pitch = []

lth = [0]
uth = [0]
ugv = [0]

lth_last = []
uth_last = []
ugv_last = []

fall = 0
fb = [0, 0]

directory = 'Testaufnahmen_Neu'

# open the file in the write mode
'''
with open('medfades_Data.txt', mode='w', newline='') as f:

    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(["Name;" "Max Acc;" "Min Acc;" "Max Gyro Veyl;"])

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):

            readfile = fct_def.readfile(f)
            acc_sum, vel_gyro = fct_def.print_mkr(readfile)

            csv_file_data = f'{f}; {max(acc_sum)}; {min(acc_sum)}; {max(vel_gyro)};'
            writer.writerow([csv_file_data])

'''

fct_def.analyse_csv('Testaaunahmen_neu_neu\hinten_umfallen' , "hinten umfallen")
fct_def.analyse_csv('Testaaunahmen_neu_neu\calibrations', "kalibrationen")
fct_def.analyse_csv('Testaaunahmen_neu_neu\gehen', "Gehen")
fct_def.analyse_csv('Testaaunahmen_neu_neu\sitzen_gehen_sitzen', "sitzen gehen sitzen")
fct_def.analyse_csv('Testaaunahmen_neu_neu\zusammensacken', "zusammensacken")