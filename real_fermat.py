from random import randint
from fractions import gcd
from time import time
import time
import sys
import math
from math import sqrt
from math import ceil

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    print("hey")
    y = (x + n // x) // 2
  return x

def fermat(n):
  C = 0
  if (n < 0):
    print("*************FAILURE************* \n")
    return -1,-1
  a = int(ceil(sqrt(n)))
  b2 = a*a - n
  if (b2 < 0):
    return -1,-1
  
  b = int(sqrt(b2))
  count = 0
  while b*b != b2:
    if (count %10000 == 0):
      print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
    
    #if (count >= 1000000000000000000000000000000):
      #print("******************FAIL**************** \n")
    #  return -1,-1
    a = a + 1
    b2 = a*a - n
    b = int(b2**0.5)
    count = count + 1
  p=a+b
  q=a-b
  #assert n == p * q
    #print('a=',a)
    #print('b=',b)
    #print('p=',p)
    #print('q=',q)
    #print('pq=',p*q)
  return p, q


count = 0        
inputFile = "128_bits.txt"
filename = "fermat_numbers_128bit.txt"
output = open(filename, 'w')
filename2 = "fermat_times_128bit.txt"
filename3 = "fermat_exponent128bit.txt"
exponent = open(filename3, 'w')
times = open(filename2, 'w')
input = open(inputFile, 'r')
num = 5
n = 10
for line in input:

 # p = randint(((2**num)-1), ((2**(num+1))-1))
 # q = randint(((2**num)-1), ((2**(num+1))-1))
  n = long(line);
  #for line in f:
  #n = int(line)
  t1 = time.time()
  checkp, checkq = fermat(n)
  print("P: %s. Q:%s"%(checkp,checkq))
  t2 = time.time()
  if (checkp != -1 and checkq != -1):
    times.write("%s \n"%(t2-t1))
    output.write("%s \n" %(n))
    print("DONE: %s \n"%(n))
    exponent.write("P: %s \n Q: %s"%(checkp,checkq))
  else:
    times.write("%s \n"%("FAILURE"))
    output.write("%s \n" %("FAILURE"))
    print("DONE: %s \n"%(n))
    exponent.write("P: %s \n Q: %s"%(checkp,checkq))

  
output.close()
times.close()
exponent.close()
