import transforms as tf
import numpy as np
import time

#DEG_PER_MS = 1.57
DEG_PER_MS = 0.3475
MS_PER_DEG = 1/DEG_PER_MS

def rotateSingle(servo, angle, ser):
        pulse = angleToPulse(angle)
        ser.write("#"+str(servo)+"P"+str(pulse)+"S1000\r\n")
        return

def rotate(new_angles,ser):
        pulse = []
        for angle in new_angles:
                pulse.append(angleToPulse(angle))
        
        decorated = [(abs(pulse[i]-1500),pulse[i], i) for i in range(0,len(pulse))]
        decorated.sort()
        pulse = [[d[1],d[2]] for d in decorated]
        
        output = ''
        for obj in pulse:
                output += "#"+str(obj[1])+"P"+str(obj[0])
        output += "T1000\r\n"
        ser.write(output) 

def angleToPulse(angle):
        pulse = map_range(angle,-180,180,950,2040)
        #pulse = 1500-angle*MS_PER_DEG
        return pulse

def map_range(og_value,og_min,og_max,new_min,new_max):
        og_range = og_max - og_min
        new_range = new_max - new_min
        new_value = (((og_value-og_min)*new_range)/og_range)+new_min
        return new_value

def moveToXYZ(new_pos,old_pos,ser):
        # Moves the arm to the given XYZ coordinates.
        try:
                sleep = 4;  height = 20

                transient1 = tf.rectToArm([sum(groundHog) for groundHog in zip(old_pos,[0,0,height])])
                transient2 = tf.rectToArm([sum(groundHog) for groundHog in zip(new_pos,[0,0,height])])
                new_angles = tf.rectToArm(new_pos)

                rotate(transient1,ser);time.sleep(sleep)
                rotate(transient2,ser);time.sleep(sleep)
                rotate(new_angles,ser);time.sleep(sleep)
                
                return new_pos
        except ValueError:
                print("Unable to move arm to "),;print(new_pos),
                print(" from "),;print(old_pos)
                print("Check to ensure arm can physically reach destination position.")

def openGrip(ser):
        SPEED = 1000
        PULSE = 1950
        output = "#5P"+str(PULSE)+"S"+str(SPEED)+"\r\n"
        ser.write(output)
        
def closeGrip(ser):
        SPEED = 1000
        PULSE = 1300
        output = "#5P"+str(PULSE)+"S"+str(SPEED)+"\r\n"
        ser.write(output)
