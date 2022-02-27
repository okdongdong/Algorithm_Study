# 넷이 놀기

import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
xy_set = set(tuple(map(int, input().split())) for _ in range(N))

cnt = 0
for x,y in xy_set:
    if ((x+A,y) in xy_set) and ((x,y+B) in xy_set) and ((x+A,y+B) in xy_set):
        
        cnt += 1

print(cnt)