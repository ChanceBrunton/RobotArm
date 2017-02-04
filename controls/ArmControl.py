import transforms as tf
import time

def rotate(servo, angle, ser):
        #angle = -angle
        pulse = angleToPulse(angle)
        ser.write("#"+str(servo)+"P"+str(pulse)+"S1000\r\n")
        return

def angleToPulse(angle):
        print('movement angle: '),;print('%7.2f'%angle),;print('\t'),
        pulse = map_range(angle,-180,180,950,2040)
        print('movement pusle: '),;print('%7.2f'%pulse)
        return pulse

def map_range(og_value,og_min,og_max,new_min,new_max):
        og_range = og_max - og_min
        new_range = new_max - new_min
        new_value = (((og_value-og_min)*new_range)/og_range)+new_min
        return new_value

def moveToXYZ(x,y,z,ser):
        print("moving to (%d,%d,%d)" % (x,y,z))
        theta,phi,psi,eta = tf.rectToArm(x,y,z)
        print [theta,phi,psi,eta]
        rotate(0,theta,ser)
        time.sleep(1)
        rotate(1,phi,ser)
        time.sleep(1)
        rotate(2,psi,ser)
        time.sleep(1)
        rotate(3,eta,ser)
