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

#ac.rotateSingle(2,90,ser)
ac.moveToXYZ(20,0,0,ser)
#ser.write("#1P1500S1000\r\n")
#ser.write("#2P1500S1000\r\n")
#ac.closeGrip(ser)

ser.close();
