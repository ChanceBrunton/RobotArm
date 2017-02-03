#!/usr/bin/python
import serial
import time
import ArmControl as ac

ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)
print(ser.name)
ser.write("ver\r")
inp = ser.readline()
print inp

#ser.write("#2P2000S1000\r\n")

ac.rotate(3,93.111,ser)
ac.moveToXYZ(20,0,20,ser)

ser.close();
