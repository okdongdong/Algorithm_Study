# 피보나치 수열처럼 보이지만...

from time import time
s= time()

fibo = [1,1,2] + [0]*1000000
for i in range(2, 1000000):
    fibo[i] = fibo[i-1] + fibo[i-2]

e = time()

print(e-s)