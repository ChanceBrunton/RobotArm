import math
from decimal import *
a = 17.78;b = 30.48; # upper and fore-arm lengths in centimeters
HT_LEN_CORR_FACTOR = 0.30 # height correction slope
HT_LEN_CORR_OFFSET = -5 # height correction offset
base_length = 30.48;
grip_length = 19.1;
fudge = 1.5

def rectToArm(new_pos):
        x = new_pos[0]
        y = new_pos[1]
        z = new_pos[2]
        
        d_projected = d = math.sqrt(x**2 + y**2)
        correction = HT_LEN_CORR_FACTOR*d_projected + HT_LEN_CORR_OFFSET
        z = z + grip_length - base_length + correction + fudge
	d = math.sqrt(x**2 + y**2 + z**2)
	#print('d:\t'),;print("%7.2f"%d)

	a1 = math.atan(z/math.sqrt(x**2 + y**2))
	a2 = pythagoreanTheoremAngle(b,a,d)
	a4 = pythagoreanTheoremAngle(d,a,b)
	a3 = math.pi - a4 - a2

	#print("a1:\t"),;print("%7.2f"%math.degrees(a1)),
        #print("\ta2:\t"),;print("%7.2f"%math.degrees(a2)),
        #print("\ta3:\t"),;print("%7.2f"%math.degrees(a3)),
        #print("\ta4:\t"),;print("%7.2f"%math.degrees(a4))

	theta = calculateTheta(x,y)
        phi = math.pi/2 - a1 - a2
	psi = a4 - math.pi
	#eta = math.pi - (a2+phi) - a3
	eta = a4 - phi

	# NOTE: Use Decimal library for more precision in law of cosines?

        #print("theta:\t"),;print("%7.2f"%math.degrees(theta)),
        #print("\tphi:\t"),;print("%7.2f"%math.degrees(phi)),
        #print("\tpsi:\t"),;print("%7.2f"%math.degrees(psi)),
        #print("\teta:\t"),;print("%7.2f"%math.degrees(eta))
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
        #print('')
	num = h**2 - s1**2 - s2**2
	den = -2*s1*s2
	#print('h:\t'),;print("%7.2f"%h),;print('\ts1:\t'),;print("%7.2f"%s1),;print('\ts2:\t'),;print("%7.2f"%s2)
	#print('num:\t'),;print("%7.2f"%num),;print('\tden:\t'),;print("%7.2f"%den),;print('\tratio:\t'),;print("%7.2f"%(num/den))
	theta = math.acos(num/den)
	#print("theta:\t"),;print("%7.2f"%math.degrees(theta))
	#print('')
	return theta
