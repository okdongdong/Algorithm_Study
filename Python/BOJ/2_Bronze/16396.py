# 선 그리기

import sys
input = sys.stdin.readline

N = int(input())
line = [0]*10001

for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, b):
        if line[i]:
            continue
        line[i] = 1

print(sum(line))
