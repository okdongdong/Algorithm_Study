# 문제집
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
N, M = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(M)]
pre_to_next = [[] for _ in range(N+1)]
in_degree = [0]*(N+1)
visited = [False]*(N+1)

for pre, next in problems:
    pre_to_next[pre].append(next)
    in_degree[next] += 1

solving_list = []
for i in range(1, N+1):
    if not in_degree[i]:
        solving_list.append(i)

result = []
while solving_list:
    pre = heappop(solving_list)
    result.append(pre)
    for next in pre_to_next[pre]:
        if visited[next]:
            continue

        if in_degree[next] == 1:
            heappush(solving_list, next)
            visited[next] = True
            continue
        in_degree[next] -= 1

print(*result)
