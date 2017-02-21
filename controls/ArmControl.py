import transforms as tf
import time

#DEG_PER_MS = 1.57
DEG_PER_MS = 0.3475
MS_PER_DEG = 1/DEG_PER_MS

def rotateSingle(servo, angle, ser):
        #angle = -angle
        pulse = angleToPulse(angle)
        ser.write("#"+str(servo)+"P"+str(pulse)+"S1000\r\n")
        return

def rotate(a0, a1, a2, a3, ser):
        SPEED = 1000
        output = ''
        output += "#0P"+str(angleToPulse(a0))+"S"+str(SPEED)
        output += "#1P"+str(angleToPulse(a1))+"S"+str(SPEED)
        output += "#2P"+str(angleToPulse(a2))+"S"+str(SPEED)
        output += "#3P"+str(angleToPulse(a3))+"S"+str(SPEED)
        output += "\r\n"
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

def moveToXYZ(x,y,z,ser):
        theta,phi,psi,eta = tf.rectToArm(x,y,z)
        rotate(theta,phi,psi,eta,ser)

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
