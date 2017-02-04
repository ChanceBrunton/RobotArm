import math
a = 23.812;b = 35.560; # upper and fore-arm lengths in centimeters

def rectToArm(x,y,z):
	d = math.sqrt(y**2 + z**2)

	if y != 0: a1 = math.atan(z/y)
	else: 	   a1 = math.pi/2
	a2 = pythagoreanTheoremAngle(b,a,d)
	a4 = pythagoreanTheoremAngle(d,a,b)
	a3 = math.pi - a4 - a2

	theta = calculateTheta(x,y)
	phi   = math.pi/2 - a1 - a2
	psi = -a4
	eta = math.pi - (a2+phi) - a3

	return  math.degrees(theta),math.degrees(phi),math.degrees(psi),math.degrees(eta)

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
def pythagoreanTheoremAngle(c,a,b):
	num = c**2 - a**2 - b**2
	den = -2*a*b
	theta = math.acos(num/den)
	return theta
