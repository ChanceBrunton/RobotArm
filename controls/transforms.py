import math
a = 1;b = 2;

def rectToArm(x,y,z):
	d = math.sqrt(y**2 + z**2)

	if y != 0: a1 = math.atan(z/y)
	else: 	   a1 = math.pi/2
	a2 = pythagoreanTheoremAngle(b,a,d)
	a4 = pythagoreanTheoremAngle(d,a,b)
	a3 = math.pi - a4 - a2

	theta = calculateTheta(x,y)
	phi   = math.pi/2 - a1 - a2
	eta = math.pi - (a2+phi) - a3
	psi = math.pi - a4

	return  math.degrees(theta),math.degrees(phi),math.degrees(psi),math.degrees(eta)

def calculateTheta(x,y):
	if x == 0:
		if y >= 0: theta = math.pi/2
		else:      theta = 3*math.pi/2
	elif x < 0:
		theta = math.atan(y/x) + math.pi
	else:
		if y >= 0: theta = math.atan(y/x)
		else:      theta = math.atan(y/x) + 2*math.pi
	return theta

# pythagoreanTheoremAngle
# Calculates the angle opposite side C of a triangle given the lengths of all sides.
def pythagoreanTheoremAngle(c,a,b):
	num = c**2 - a**2 - b**2
	den = -2*a*b
	theta = math.acos(num/den)
	return theta