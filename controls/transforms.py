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
HT_LEN_CORR_FACTOR = 0.18 # height correction slope
HT_LEN_CORR_OFFSET = -2.6 # height correction offset
base_length = 30.48;
grip_length = 20.955;

def rectToArm(X):
        X = list(X)
        d_projected = math.sqrt(X[0]**2 + X[1]**2)
        correction = HT_LEN_CORR_FACTOR*d_projected + HT_LEN_CORR_OFFSET
        X[2] = X[2] + grip_length - base_length + correction
	d = math.sqrt(X[0]**2 + X[1]**2 + X[2]**2)

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

	theta = calculateTheta(X[0],X[1])
        phi = math.pi/2 - a1 - a2
	psi = a4 - math.pi
	eta = a4 - phi
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
