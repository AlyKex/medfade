import time
import serial

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


