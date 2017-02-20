from random import randint
from time import time
import time
def gcd(x,y):
	if y==0:
		return x
	else:
		return gcd(y,x%y)
def g(x,n):
	return (x*x+2)%n

def pollardrho(a):
	x = 2
	y = 2
	d = 1
	while d == 1:
		x = g(x,a)
		y = g(g(y,a,),a)
		d = gcd(abs(x-y),a)
		print x,y,d
		
		if d > 1 and a > d:
			return d
		if d == a:
			return -1
count = 0
num = 5
inputFile = "128_bits.txt"
filename = "pollard_numbers128bit.txt"
filename2 = "pollard_time128bit.txt"
filename3 = "pollard_exponent128bit.txt"
output = open(filename, 'w')
times = open(filename2, 'w')
exponent = open(filename3, 'w')
input = open(inputFile,'r')
for line in input:
	#p = randint(((2**num)-1), ((2**(num+2))-1))
	#q = randint(((2**num)-1), ((2**(num+2))-1))
	#n = p*q
	n = long(line);
        t1 = time.time()
        d = pollardrho(n)
        t2 = time.time()
        times.write("%s \n"%(t2-t1))
	output.write("%s \n"%(n))
	print("%s \n"%(n))
	exponent.write("%s \n"%(d))
        print("DONE: %s \n"%(n))
	
	#t1 = time.time()
	#a = pollardrho(n)
	#t2 = time.time()
	#b = (p*q)/a
	#output.write("%s \n"%(n))
	#output.write("\n")
	#times.write("%s \n"%(t2-t1))
	#times.write("\n")
	#print('factors: %s, %s' %(a,b))
