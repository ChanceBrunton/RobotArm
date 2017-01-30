#!/usr/bin/python
import serial
import time
import ArmControl

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)
print(ser.name)
ser.write("ver\r")
inp = ser.readline()
print inp

ser.write("#1P1780S1000\r\n")

#ArmControl.rotate(3,0,ser)
#print(ArmControl.map_range(90,0,10,0,100))

ser.close();
