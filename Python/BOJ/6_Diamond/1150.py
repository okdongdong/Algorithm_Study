from heapq import heapify, heappop, heappush
import sys

input = sys.stdin.readline
N, K = map(int, input().split())

distances = [0] + [int(input()) for _ in range(N)] + [0]
que = []
visited = [False] * (N + 1)

for i in range(1, N):
    que.append((distances[i + 1] - distances[i], i, i + 1))

heapify(que)

connected_distances = []

while len(connected_distances) < K:
    distance, a, b = heappop(que)

    if a == 0 or b == N + 1 or visited[a] or visited[b] or :
        continue

    visited[a] = True
    visited[b] = True
    connected_distances.append(distance)

    distance_a = distances[a] - distances[a - 1]
    distacne_b = distances[b + 1] - distances[b]

    heappush(que, (distance_a + distacne_b - distance, a - 1, b + 1))

print(sum(connected_distances))
