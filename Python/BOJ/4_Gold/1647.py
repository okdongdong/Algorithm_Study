# 도시 분할 계획

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [0]*(N+1)
roads = [[] for _ in range(N+1)]
now_house = 1
min_cost = 99999999999999
for _ in range(M):
    A, B, C = map(int, input().split())
    roads[A].append((C, B))
    roads[B].append((C, A))
    if min_cost > C:
        min_cost = C
        now_house = A
visited[now_house] = 1

target_house = []
for i in roads[now_house]:
    heappush(target_house, i)

sum_cost = 0
max_cost = 0

for _ in range(N-1):
    while True:
        cost, target = heappop(target_house)
        if not visited[target]:
            break
    
    visited[target] = cost
    sum_cost += cost
    if cost > max_cost:
        max_cost = cost

    for i in roads[target]:
        if visited[i[1]]:
            continue
        heappush(target_house, i)

print(sum_cost-max_cost)