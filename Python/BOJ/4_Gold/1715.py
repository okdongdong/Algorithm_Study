# 카드정렬하기

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    heappush(heap, int(input()))
result = 0
while len(heap) > 1:
    num1 = heappop(heap)
    num2 = heappop(heap)
    result += num1 + num2
    heappush(heap, num1+num2)

print(result)
