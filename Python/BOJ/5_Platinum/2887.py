# 행성 터널
import sys
from heapq import heappop, heappush
input = sys.stdin.readline


def add_edges(positions):
    for i in range(N-1):
        val1, idx1 = positions[i]
        val2, idx2 = positions[i+1]
        edges[idx1].append((abs(val1 - val2), idx2))
        edges[idx2].append((abs(val1 - val2), idx1))


N = int(input())
INF = int(10e9)

x_positions = []
y_positions = []
z_positions = []

for idx in range(N):
    x, y, z = map(int, input().split())
    x_positions.append((x, idx))
    y_positions.append((y, idx))
    z_positions.append((z, idx))

x_positions.sort()
y_positions.sort()
z_positions.sort()

edges = [[] for _ in range(N)]

add_edges(x_positions)
add_edges(y_positions)
add_edges(z_positions)

que = [(0, 0)]
visited = [False]*N
result, cnt = 0, 0


while que and cnt < N:
    val1, idx1 = heappop(que)
    if visited[idx1]:
        continue

    visited[idx1] = True
    result += val1

    for val2, idx2 in edges[idx1]:
        heappush(que, (val2, idx2))

    cnt += 1

print(result)

# planets = [list(map(int, input().split())) for _ in range(N)]
# next_planet_list = set(range(1, N))
# now_planet = 0
# costs = []
# cnt = 1
# result = 0
# while cnt < N:
#     x, y, z = planets[now_planet]
#     now_cost1, now_cost2 = (2000000001, 0), (2000000001, 0)
#     for next_planet in next_planet_list:
#         nx, ny, nz = planets[next_planet]
#         now_cost = (min(map(abs, [x-nx, y-ny, z-nz])), next_planet)
#         now_cost1, now_cost2 = sorted([now_cost1, now_cost2, now_cost])[:2]

#         heappush(costs, (now_cost1))
#         heappush(costs, (now_cost2))

#     cost, now_planet = heappop(costs)
#     next_planet_list.remove(now_planet)
#     result += cost
#     cnt += 1
#     temp = []
#     for i in range(len(costs)):
#         if costs[i][1] not in next_planet_list:
#             continue
#         temp.append(costs[i])
#     costs = temp

# print(result)
