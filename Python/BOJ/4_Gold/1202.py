# 보석 도둑
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, K = map(int, input().split())

gems = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
gems.sort()
bags.sort()
gem_idx = 0

temp = []
result = 0
for i in range(K):
    while gem_idx < N and bags[i] >= gems[gem_idx][0]:
        heappush(temp, -gems[gem_idx][1])
        gem_idx += 1
    
    if temp:
        result -= heappop(temp)

print(result)