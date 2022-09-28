# Importing Libraries
import serial
#import pyplot


data = []
ser = serial.Serial(port='COM4', baudrate=2000000, timeout=2)

sensvalraw = ser.readline()

while len(data)<10:
    sensvalraw = ser.readline()

    sensvalstring = sensvalraw.decode()
    sensvalstripped = sensvalstring.strip()

    sensvalsplit = sensvalstripped.split(';')

    data.append(float(sensvalsplit[0]))
    data.append(float(sensvalsplit[1]))
    data.append(float(sensvalsplit[2]))


print(data)
ser.close()




