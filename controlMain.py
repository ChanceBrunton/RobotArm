 #!/usr/bin/python
import serial
import time
import ArmControl as ac
import transforms as tf
from Utility import *
from TestRoutines import *
import math
import socket

# serial communication
ser = serial.Serial('/dev/ttyUSB0',baudrate=9600,timeout=2)

# socket communication
server_address = ('localhost',5001)

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    sock.sendall('Picture')
    objString = sock.recv(1024)
    print objString
    sock.close

# intial position
#initial_pos = [20,0,30]; # 17 inches
#current_pos = list(initial_pos);
#ac.rotate(tf.rectToArm(list(initial_pos)),ser);
#time.sleep(2)

# variables
goal_pos = [45,0,10] # 12 inches
obj_pos = [30,0,0] # 5 inches


