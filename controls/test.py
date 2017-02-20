import math
from decimal import *

def pythagoreanTheoremAngle1(h,s1,s2):
        print('')
        print(type(h));
        print(type(s1));
        print(type(s2));
	num = h**2 - s1**2 - s2**2
	print(type(num));
	den = -2*s1*s2
	print(type(den));
	#print('h:\t'),;print("%64.64f"%h);print('\ts1:\t'),;print("%7.2f"%s1),;print('\ts2:\t'),;print("%7.2f"%s2)
	#print('num:\t'),;print("%64.64f"%num);print('\tden:\t'),;print("%7.2f"%den),;print('\tratio:\t'),;print("%7.2f"%(num/den))
        frac = num/den;#print("frac:\t"),;print("%64.64f"%frac)
        print(type(frac));
	theta = math.acos(frac)
	print(type(theta));
	#print("theta:\t"),;print("%64.64f"%theta)
        print('')
	return theta

def pythagoreanTheoremAngle2(h,s1,s2):
        getcontext().prec = 100
        print getcontext()
        h = Decimal(h)
        s1 = Decimal(s1)
        s2 = Decimal(s2)
        print('')
	num = h**2 - s1**2 - s2**2
	den = -2*s1*s2
	#print('h:\t'),;print("%64.64f"%h);print('\ts1:\t'),;print("%7.2f"%s1),;print('\ts2:\t'),;print("%7.2f"%s2)
	#print('num:\t'),;print("%64.64f"%num);print('\tden:\t'),;print("%7.2f"%den),;print('\tratio:\t'),;print("%7.2f"%(num/den))
	frac = num/den;#print("frac:\t"),;print("%64.64f"%frac)
	theta = math.acos(frac)
	#print("theta:\t"),;print("%64.64f"%theta)
        print('')
        #print(s2)
	return theta

a = 23.97; b = 35.4; d = 20
print(pythagoreanTheoremAngle1(d,a,b))
print(Decimal(pythagoreanTheoremAngle1(d,a,b)))
pythagoreanTheoremAngle2(d,a,b)

