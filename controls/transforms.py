import math
from decimal import *

#########################################
# Image Coordinate Mapping
#########################################
FOCAL_LENGTH = 3600.0 # micrometers
PX_SIZE = 1.4 #micrometers
X_PIXELS = 2592
Y_PIXELS = 1944
IMG_RES = 256

def convertCamX(camX,height):
        (PX_SIZE*height*camX*X_PIXELS) / (FOCAL_LENGTH*IMG_RES)

def convertCamY(camY,height):
        (PX_SIZE*height*camY*Y_PIXELS) / (FOCAL_LENGTH*IMG_RES)

#########################################
# Rectangular/Arm Coordinate Transforms
#########################################
a = 17.78;b = 30.48; # upper and fore-arm lengths in centimeters
#SLOPE = 0.1832   # height correction slope
SLOPE = 3.8
#OFFSET = -1.5875 # height correction offset
OFFSET = -21
base_length = 30.48;
grip_length = 20.955;
MIN_DIST = 13;

def rectToArm(X): 
        X = list(X) # copy list so as not to modify original

        # calculate distance from destination
        d_projected = math.sqrt(X[0]**2 + X[1]**2)
        d = math.sqrt(X[0]**2 + X[1]**2 + X[2]**2)

        #TODO:
        # The arm is 5/8" above where it should be at 14,0,0 and
        # 1.25" below where it should be at 40,0,0 without correction factors

        # apply linear corrective term to arm height
        #corrective_line = OFFSET + SLOPE*math.sqrt(d_projected)
        #X[2] = X[2] + corrective_line

        # adjust for base height and grip length
        #X[2] = X[2] + grip_length - base_length
	
	a1 = math.atan(X[2]/math.sqrt(X[0]**2 + X[1]**2))

	try:
                a2 = pythagoreanTheoremAngle(b,a,d)
        except ValueError as err:
                raise ValueError('failed computing a2 with (%f,%f,%f)\n\t'%(b,a,d)+str(err))

        try:
                a4 = pythagoreanTheoremAngle(d,a,b)
        except ValueError as err:
                raise ValueError('failed computing a4 with (%f,%f,%f)\n\t'%(d,a,b)+str(err))
	
	a3 = math.pi - a4 - a2

        print('%5.2f %5.2f %5.2f %5.2f'%(math.degrees(a1),\
                                         math.degrees(a2),\
                                         math.degrees(a3),\
                                         math.degrees(a4)))

	theta = calculateTheta(X[0],X[1])
        phi = math.pi/2 - a1 - a2
	psi = a4 - math.pi
	eta = a4 - phi

	print('recieved [%d, %d, %d, %d]'%(math.degrees(theta),\
                                           math.degrees(phi),\
                                           math.degrees(psi),\
                                           math.degrees(eta)))
	
	return  math.degrees(theta),\
                math.degrees(phi),\
                -math.degrees(psi),\
                -math.degrees(eta)

def calculateTheta(x,y):
	if x == 0:
		if y >= 0: theta = math.pi/2
		else:      theta = -math.pi/2
	elif x < 0:
                if y < 0:
                        theta = math.atan(y/x) + math.pi
                else:
                        theta = math.atan(y/x) - math.pi
	else:
                theta = math.atan(y/x)
	return theta

# pythagoreanTheoremAngle
# Calculates the angle opposite side C of a triangle given the lengths of all sides.
def pythagoreanTheoremAngle(h,s1,s2):
	num = h**2 - s1**2 - s2**2
	den = -2*s1*s2
	try:
                theta = math.acos(num/den)
        except ValueError:
                raise ValueError('Pythagorean Theorem - Cannot compute acos(%f/%f)'%(num,den))
	return theta
