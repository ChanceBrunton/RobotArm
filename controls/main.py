#!/usr/bin/python
import serial
import time
import ArmControl as ac
import transforms as tf
from Utility import *
from TestRoutines import *
import math

# serial communication
ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)

# intial position
initial_pos = [20,0,30]; # 17 inches
current_pos = list(initial_pos);
#ac.rotate(tf.rectToArm(list(initial_pos)),ser);
time.sleep(2)

# goal box position # 12 inches
goal_pos = [45,0,10]

# object position
obj_pos = [30,0,0] # 5 inches

# test arm
######## NOTE: TODO: Use 'logging' instead of print for debug statements
loopTest(current_pos,ser)
#repeatPickupTest(current_pos,initial_pos,obj_pos,goal_pos,ser)

#theta = 0
#phi = -21
#psi = 143
#eta = -56
#dPhi,dPsi = tf.calculateOffsets(math.radians(phi),math.radians(psi))
#print(str(dPhi)+"\t"+str(dPsi))
#ser.write("#0P"+str(ac.angleToPulse(theta))+"S100\r\n")
#ser.write("#1P"+str(ac.angleToPulse(phi+math.degrees(dPhi)))+"S100\r\n")
#ser.write("#2P"+str(ac.angleToPulse(psi+math.degrees(dPsi)))+"S100\r\n")
#ser.write("#3P"+str(ac.angleToPulse(eta))+"S100\r\n")
#ser.close();
