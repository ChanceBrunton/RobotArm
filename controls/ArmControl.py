import transforms as tf
import numpy as np
import time
import traceback
import math

DEG_PER_MS = 1.57/5
MS_PER_DEG = 1/DEG_PER_MS

def rotateSingle(servo, angle, ser):
        pulse = angleToPulse(angle)
        print('Sending servo %d to angle %.1f with pulse %.1f'%(servo,angle,pulse))
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
        pulse = 1500+angle*MS_PER_DEG
        return pulse

def map_range(og_value,og_min,og_max,new_min,new_max):
        og_range = og_max - og_min
        new_range = new_max - new_min
        new_value = (((og_value-og_min)*new_range)/og_range)+new_min
        return new_value

def moveToXYZ(new_pos,current_pos,ser):
        # Moves the arm to the given XYZ coordinates.
        try:
                sleep = 5;  height = 20
                neutral_pt = [30,0,40]

                print("initial current_pos "),; print current_pos
                print("initial new_pos "),; print new_pos

                # calculate the initial height clearances
                maxArmHeight = 48 # maximum height the arm can reach
                armReach = 34 # total length over which the arm can reach
                h1 = maxArmHeight - (maxArmHeight/armReach)*math.sqrt(current_pos[0]**2 + current_pos[1]**2)
                h2 = maxArmHeight - (maxArmHeight/armReach)*math.sqrt(new_pos[0]**2 + new_pos[1]**2)

                print('h1 = %7.4f\th2 = %7.4f'%(h1,h2))

                try:
                        dest1 = [current_pos[0],current_pos[1],h1] # use transient height over old position
                        transient1 = tf.rectToArm(dest1)
                except ValueError as err:
                        raise ValueError('Unable to move to move to [%s,%s,%s]\n\t'%tuple(dest1)+str(err))

                try:
                        dest2 = [new_pos[0],new_pos[1],h2] # use transient height over new position
                        transient2 = tf.rectToArm(dest2)
                except ValueError as err:
                        raise ValueError('Unable to move to move to [%s,%s,%s]\n\t'%tuple(dest2)+str(err))

                try:
                        new_angles = tf.rectToArm(new_pos)
                except ValueError as err:
                        raise ValueError('Unable to move to move to [%s,%s,%s]\n\t'%tuple(new_angles)+str(err))

                print("final current_pos "),; print current_pos
                print("final new_pos "),; print new_pos

                rotate(transient1,ser);time.sleep(sleep)
                rotate(transient2,ser);time.sleep(sleep)
                rotate(new_angles,ser);time.sleep(sleep)
                
                return new_pos
        except ValueError as err:
                print("Unable to move arm to [%s, %s, %s]"%tuple(new_pos)),
                print(" from [%s, %s, %s]"%tuple(current_pos))
                print("ValueError: "),;print(err)
                #traceback.print_exc()

def openGrip(ser):
        SPEED = 1000
        PULSE = 1950
        output = "#5P"+str(PULSE)+"S"+str(SPEED)+"\r\n"
        ser.write(output)
        time.sleep(1)
        
def closeGrip(ser):
        SPEED = 1000
        PULSE = 1300
        output = "#5P"+str(PULSE)+"S"+str(SPEED)+"\r\n"
        ser.write(output)
        time.sleep(1)
