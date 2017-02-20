from random import randint
from fractions import gcd
from time import time
import time
import sys
import math

#from math import ceil


def Rabin(num,num2):
    prime = False
    while (prime == False):
        n = randint(((2**num)-1), ((2**num2)-1))
        while (n%2 == 0):
            n = randint(((2**num)-1), ((2**num2)-1))
        
        k = 0;
        m = 0;
        ndiv = n - 1
        
        while ((ndiv % 2) == 0):
            ndiv = ndiv/2
            k = k+1
        count = 0        
        check = 0
        m = ndiv
        while(check < 10):
            count = count + 1
            if (count > 200):
                check = 11
            a = randint(1,n)
            #print('a: %d' %a)
            #print('n: %d' %n)
        #    print('m: %d' %m)
            #print('k: %d' %k)
        #    print('a: %d'%a)
            b = a**m
            b = b % n
        #    print('b %d' %b)
            if ((b-1) %n == 0):

                check = check + 1
                #print('ADD 1 FIRST')
            i = 0
            for i in range(k):
                #print('b: %d' %b)
                if ((b+1)%n == 0):
                    check = check +1
                   # print('ADD 1 SECOND')
                else:
                    b = (b**2) % n
        if (check >= 11):
            #print(".")
            prime = False
        else:
            prime = True
        
        
    #print('FOUND PRIME N')
    #print('PRIME: %d ' %n)
    return n
        
filename = "Numbers.txt"
output = open(filename, 'w')
filename2 = "Factors.txt"
factors = open(filename2, 'w')
#n = randint(((2**15)-1), ((2**16)-1))
#while (n%2 == 0):
#    n = randint(((2**15)-1), ((2**16)-1))
num = 5
count = 0
while (True):
  p = Rabin(num,num+1)        
  q = Rabin(num,num+1)
  output.write(" %s \n"%(p*q))
  factors.write("%s %s \n" %(p,q))
  if (count % 15 == 0):
    num = num + 1
  count = count+1
  print("%s" %(p*q))
