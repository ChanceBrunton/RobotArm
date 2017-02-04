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

#ac.rotate(0,-90,ser)
#ac.rotate(1,0.635,ser)
#ac.rotate(2,0,ser)
#ac.rotate(3,0,ser)
ac.moveToXYZ(20,20,20,ser)

ser.close();
