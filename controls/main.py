#!/usr/bin/python
import serial
import time
import ArmControl as ac
import transforms as tf
from Utility import *

# serial communication
ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)

# intial position
initial_pos = [43.18,0,10]; # 17 inches
current_pos = initial_pos;
ac.rotate(tf.rectToArm(initial_pos),ser);

# goal box position # 12 inches
goal_pos = [30,0,10]

# object position
obj_pos = [12.7,0,0] # 5 inches

# move arm until program ends
while True:
    try:
        new_pos = read_coords()
        ac.openGrip(ser)
        current_pos = ac.moveToXYZ(new_pos,current_pos,ser)
        ac.closeGrip(ser)

        #ac.openGrip(ser)        
        #current_pos = ac.moveToXYZ(obj_pos,current_pos,ser)
        #ac.closeGrip(ser)
        #current_pos = ac.moveToXYZ(goal_pos,current_pos,ser)
        #ac.openGrip(ser)
        #current_pos = ac.moveToXYZ(initial_pos,current_pos,ser)
        #ac.closeGrip(ser)
    except ValueError as err:
        print('ValueError: '),;print(err)
        
ser.close();

