#!/usr/bin/python
import serial
import time
import ArmControl as ac
import transforms as tf

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)
print(ser.name)
ser.write("ver\r")
inp = ser.readline()
print inp

#ac.rotateSingle(5,0,ser)
ac.moveToXYZ(0,-50,40,ser)
#ser.write("#5P1300S1000\r\n")
#ac.closeGrip(ser)

ser.close();
