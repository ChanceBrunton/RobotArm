#!/usr/bin/python
import serial
import time
import ArmControl as ac
import transforms as tf

# serial communication
ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)

# intial position
initialPosition = [30,0,10];
current_pos = initialPosition;
ac.rotate(tf.rectToArm(initialPosition),ser);

# move arm until program ends
while True:
    new_pos = input("Position ('[x,y,z]'): ")
    ac.openGrip(ser)
    current_pos = ac.moveToXYZ(new_pos,current_pos,ser)
    ac.closeGrip(ser)
ser.close();
