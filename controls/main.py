#!/usr/bin/python
import serial
import time
import ArmControl as ac
import transforms as tf

current_pos = [40,0,3]

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)
print(ser.name)
ser.write("ver\r")
inp = ser.readline()
print inp

#ac.rotateSingle(2,90,ser)
new_pos = [14,0,3]
current_pos = ac.moveToXYZ(new_pos,current_pos,ser)
#ser.write("#1P1500S1000#2P1500S1000#3P1500S1000#4P1500S1000\r\n")
#ser.write("#2P1500S1000\r\n")
#ac.closeGrip(ser)

ser.close();
