import time
import serial
import os
import fct_def
import csv
import matplotlib.pyplot as plt

def writefile(data_to_write):
    cTime = time.strftime("%d_%m_%Y__%H_%M_%S")
    with open(F"{cTime}", 'w', encoding='UTF8') as f:
        f.writelines('\n'.join(data_to_write))
    return cTime


def readfile(fname):
    with open(F"{fname}", 'r', encoding='UTF8') as f:
        return (f.read())


def printfile(rdata):
    data_lin_x, data_lin_y, data_lin_z, data_lin_sum = [], [], [], []

    data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum = [], [], [], []

    data_orient_grad_x, data_orient_grad_y, data_orient_grad_z = [], [], []

    data_et = []


    sensval_devided = rdata.split(",")
    sensval_len = len(sensval_devided)
    for i in range(sensval_len):

        sensvalstripped = sensval_devided[i].strip()
        sensvalsplit = sensvalstripped.split(" ")

        if "lb" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_x.append(float(sensvalsplit[0]))
            data_lin_y.append(float(sensvalsplit[1]))
            data_lin_z.append(float(sensvalsplit[2]))

            data_lin_sum.append(float(sensvalsplit[0]) + float(sensvalsplit[1]) + float(sensvalsplit[2]))


        elif "lk" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_kor_x.append(float(sensvalsplit[0]))
            data_lin_kor_y.append(float(sensvalsplit[1]))
            data_lin_kor_z.append(float(sensvalsplit[2]))
            data_lin_kor_sum.append(float(sensvalsplit[0]) + float(sensvalsplit[1]) + float(sensvalsplit[2]))


        elif "ow" in sensvalsplit:
            del sensvalsplit[0]
            data_orient_grad_x.append(float(sensvalsplit[0]))
            data_orient_grad_y.append(float(sensvalsplit[1]))
            data_orient_grad_z.append(float(sensvalsplit[2]))
        elif "et" in sensvalsplit:
            data_et.append(float(sensvalsplit[1]))
            return data_lin_x, data_lin_y, data_lin_z, data_lin_sum, data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum, data_orient_grad_x, data_orient_grad_y, data_orient_grad_z, data_et

def readserport():
    data_lin_x, data_lin_y, data_lin_z, data_lin_sum = [], [], [], []

    data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum = [], [], [], []

    data_orient_grad_x, data_orient_grad_y, data_orient_grad_z = [], [], []

    data_et = []

    sensvalstrip_save = []

    ser = serial.Serial(port='COM7', baudrate=2000000, timeout=1)
    while True:
        sensvalraw = ser.readline()
        sensvalstring = sensvalraw.decode()

        print(sensvalstring)
        if "abc" in sensvalstring:
            break

    start = time.time()
    while True:
        sensvalraw = ser.readline()
        sensvalstring = sensvalraw.decode()
        sensvalstrip = sensvalstring.strip()

        sensvalstrip_save.append(F"{sensvalstrip},")

        sensvalsplit = sensvalstrip.split()

        if "lb" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_x.append(float(sensvalsplit[0]))
            data_lin_y.append(float(sensvalsplit[1]))
            data_lin_z.append(float(sensvalsplit[2]))

            data_lin_sum.append(float(sensvalsplit[0]) + float(sensvalsplit[1]) + float(sensvalsplit[2]))


        elif "lk" in sensvalsplit:
            del sensvalsplit[0]
            data_lin_kor_x.append(float(sensvalsplit[0]))
            data_lin_kor_y.append(float(sensvalsplit[1]))
            data_lin_kor_z.append(float(sensvalsplit[2]))
            data_lin_kor_sum.append(float(sensvalsplit[0]) + float(sensvalsplit[1]) + float(sensvalsplit[2]))


        elif "ow" in sensvalsplit:
            del sensvalsplit[0]
            data_orient_grad_x.append(float(sensvalsplit[0]))
            data_orient_grad_y.append(float(sensvalsplit[1]))
            data_orient_grad_z.append(float(sensvalsplit[2]))

        elif "et" in sensvalsplit:
            data_et.append(float(sensvalsplit[1]))
            break
    ser.close()
    return start, data_lin_x, data_lin_y, data_lin_z, data_lin_sum, data_lin_kor_x, data_lin_kor_y, data_lin_kor_z, data_lin_kor_sum, data_orient_grad_x, data_orient_grad_y, data_orient_grad_z, data_et, sensvalstrip_save

def readserport_mkr():

    acc_sum = []
    vel_gyro = []
    sensvalstrip_save = []


    ser = serial.Serial(port='COM7', baudrate=2000000, timeout=1)
    while True:
        sensvalraw = ser.readline()
        sensvalstring = sensvalraw.decode()

        print(sensvalstring)
        if "abc" in sensvalstring:
            break

    while True:


        sensvalraw = ser.readline()
        sensvalstring = sensvalraw.decode()
        sensvalstrip = sensvalstring.strip()

        sensvalstrip_save.append(F"{sensvalstrip},")

        if "ex" in sensvalstrip:
            break

        sensvalsplit = sensvalstrip.split()

        acc_sum.append(float(sensvalsplit[0]))
        vel_gyro.append(float(sensvalsplit[1]))

    ser.close()
    return acc_sum, vel_gyro, sensvalstrip_save

def print_mkr(readfile):

    acc_sum = []
    vel_gyro = []

    data_split = readfile.split(",")

    for i in range(len(data_split)):
        data_strip = data_split[i].strip()
        data = data_strip.split()

        if "ex" in data:
            break

        acc_sum.append(float(data[0]))
        vel_gyro.append(float(data[1]))

    return acc_sum, vel_gyro


def readserport_mkr_mega():

    sensvalstrip_save = []


    ser = serial.Serial(port='COM7', baudrate=2000000, timeout=1)
    while True:
        sensvalraw = ser.readline()
        sensvalstring = sensvalraw.decode()

        print(sensvalstring)
        if "start" in sensvalstring:
            break

    while True:


        sensvalraw = ser.readline()
        sensvalstring = sensvalraw.decode()
        sensvalstrip = sensvalstring.strip()

        sensvalstrip_save.append(F"{sensvalstrip},")

        if "ex" in sensvalstrip:
            break



    ser.close()
    return sensvalstrip_save


def print_mkr_mega(readfile):

    acc_sum = []
    vel_gyro = []
    heading = []
    roll = []
    pitch = []

    data_split = readfile.split(",")

    for i in range(len(data_split)):
        data_strip = data_split[i].strip()
        data = data_strip.split()

        if "ex" in data:
            break

        acc_sum.append(float(data[0]))
        vel_gyro.append(float(data[1]))
        heading.append(float(data[2]))
        roll.append(float(data[3]))
        pitch.append(float(data[4]))

    return acc_sum, vel_gyro, heading, roll, pitch


def analyse_csv(directory, name):

    lth_last = []
    uth_last = []
    head_d, roll_d, pitch_d, lu_d = 0, 0, 0, 0

    name += ".txt"

    with open(name, mode='w', newline='') as f:
        writer = csv.writer(f)


        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):

                readfile = fct_def.readfile(f)
                acc_sum, vel_gyro, heading, roll, pitch = fct_def.print_mkr_mega(readfile)

                for i in range(len(acc_sum)):
                    if acc_sum[i] <= 2.8:
                        lth_last.append(i)

                    if acc_sum[i] >= 65:
                        uth_last.append(i)


                if len(uth_last) > 0:
                    uth_t = uth_last[0]
                    head_d = abs(heading[uth_t] - heading[0])
                    roll_d = abs(roll[uth_t] - roll[0])
                    pitch_d = abs(pitch[uth_t] - pitch[0])
                    if len(lth_last) > 0:
                        lu_d = uth_last[0] - lth_last[len(lth_last) - 1]

                    else:
                        lu_d = 0

                else:
                    head_d, roll_d, pitch_d = 0, 0, 0

                f.strip()
                f = os.path.basename(os.path.normpath(f))
                f = name
                csv_file_data = f'{max(acc_sum)}; {min(acc_sum)}; {max(vel_gyro)}; {lu_d}; {head_d}; {roll_d}; {pitch_d};'
                writer.writerow([csv_file_data])

def analyse_csv_old(directory, name):
    name += ".txt"

    lth_last = []
    uth_last = []
    bp_test = []

    with open(name, mode='w', newline='') as f:
        writer = csv.writer(f)

        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):

                readfile = fct_def.readfile(f)
                acc_sum, vel_gyro = fct_def.print_mkr(readfile)

                for i in range(len(acc_sum)):
                    if acc_sum[i] <= 2.8:
                        lth_last.append(i)

                    if acc_sum[i] >= 65:
                        uth_last.append(i)

                f.strip()
                f = os.path.basename(os.path.normpath(f))
                f = name
                csv_file_data = f'{max(acc_sum)}; {min(acc_sum)}; {max(vel_gyro)};'
                writer.writerow([csv_file_data])
                bp_test.append(min(acc_sum))
