# 행성 터널
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
planets = [list(map(int, input().split())) for _ in range(N)]
next_planet_list = set(range(1, N))
now_planet = 0
costs = []
cnt = 1
result = 0
while cnt < N:
    x, y, z = planets[now_planet]
    now_cost1, now_cost2 = (2000000001, 0), (2000000001, 0)
    for next_planet in next_planet_list:
        nx, ny, nz = planets[next_planet]
        now_cost = (min(map(abs, [x-nx, y-ny, z-nz])), next_planet)
        now_cost1, now_cost2 = sorted([now_cost1, now_cost2, now_cost])[:2]

        heappush(costs, (now_cost1))
        heappush(costs, (now_cost2))

    cost, now_planet = heappop(costs)
    next_planet_list.remove(now_planet)
    result += cost
    cnt += 1
    temp = []
    for i in range(len(costs)):
        if costs[i][1] not in next_planet_list:
            continue
        temp.append(costs[i])
    costs = temp

print(result)
