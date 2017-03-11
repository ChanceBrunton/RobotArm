#!/usr/bin/python
import serial
import time
import ArmControl as ac
import transforms as tf
from Utility import *
from TestRoutines import *

# serial communication
ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)

# intial position
initial_pos = [20,0,30]; # 17 inches
current_pos = list(initial_pos);
#ac.rotate(tf.rectToArm(list(initial_pos)),ser);
time.sleep(2)

# goal box position # 12 inches
goal_pos = [30,0,10]

# object position
obj_pos = [12.7,0,0] # 5 inches

# test arm
#loopTest(current_pos,ser)
#repeatPickupTest(current_pos,initial_pos,obj_pos,goal_pos,ser)
#ac.rotateSingle(3,0,ser)
ser.write("#0P"+str(ac.angleToPulse(0))+"S10\r\n")
ser.write("#1P"+str(ac.angleToPulse(90))+"S10\r\n")
ser.write("#2P"+str(ac.angleToPulse(0))+"S10\r\n")
ser.write("#3P"+str(ac.angleToPulse(0))+"S10\r\n")
ser.close();
