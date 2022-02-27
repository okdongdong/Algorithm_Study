# 일단포기..

import sys
from time import time

input = sys.stdin.readline

T = int(input())
R = list(map(int, input().split()))

s = time()

min_K_list=[]
for r in range(1, 10):
    num = 2
    k = 1
    while True:
        num *= 16
        k += 4
        num_str = str(num)
        
        if len(num_str) < r:
            continue
        
        num_str = num_str[-r:]
        
        for ns in num_str:
            if not (ns == '1' or ns == '2'):
                break
        else:
            min_K_list.append(k)
            break
        
        num = int(num_str)

print(min_K_list)

e = time()

print(e-s)