#from math import ceil
from time import time
import time
def isqrt(n):
  x = n
  #Using floor divide, computer y
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  #print('returning %s'%(x))
  return x

def fermat(n):
  
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    #Check for square
    while b*b != b2:
      
            #print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
      a = a + 1
      b2 = a*a - n
      b = isqrt(b2) # int(b2**0.5)
      count += 1
    p=a+b
    q=a-b
    assert n == p * q
    #print('a=',a)
    #print('b=',b)
    #print('p=',p)
    #print('q=',q)
    #print('pq=',p*q)
    return p, q

count = 0;
n = 131079
a = 2
b = 1
filename = "output2.txt"
filename2 = "Numbers2.txt"
filename3 = "Time2.txt"
target = open(filename, 'w')
nums = open(filename2, 'w')
times = open(filename3, 'w')
target.truncate()
while(n < 1000000000000):
  print('Trying : %s ' %(n))
  if (n%2 == 0):
    n = n +1
    
  if(n%2 == 0):
    print('whoops')
  
  t1 = time.time()
  fermat(n)
  t2 = time.time()
  doneTime = t2-t1
  print('Ran in: %s ' %(doneTime))
  print('Done this many: %s' %(count))
  target.write('Num: %s  Time: %s' %(n,doneTime))
  target.write("\n")
  nums.write('%s'%(n))
  nums.write("\n")
  times.write('%s'%(doneTime))
  times.write("\n")
  n = n + 80000
  b = a
  a = n
  count = count+1
target.close()
nums.close()
times.close()
