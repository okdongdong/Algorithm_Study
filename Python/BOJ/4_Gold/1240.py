import sys

input = sys.stdin.readline
INF = float("inf")
N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dist[i][i] = 0

for _ in range(N - 1):
    s, e, d = map(int, input().split())
    edges[s].append((e, d))
    edges[e].append((s, d))
    dist[s][e] = d
    dist[e][s] = d

for _ in range(M):
    a, b = map(int, input().split())
    if dist[a][b] != INF:
        print(dist[a][b])
        continue

    que = [a]
    visited = [False] * (N + 1)
    visited[a] = True
    while que:
        temp = []

        for s in que:
            for e, d in edges[s]:
                if visited[e]:
                    continue

                dist[a][e] = dist[a][s] + d
                dist[e][a] = dist[a][s] + d
                visited[e] = True
                temp.append(e)

        que = temp

    print(dist[a][b])
