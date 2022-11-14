from heapq import heappop, heappush


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
islands = [[0] * M for _ in range(N)]
island_num = 1
for r in range(N):
    for c in range(M):
        if arr[r][c] and not islands[r][c]:
            stack = [(r, c)]
            while stack:
                _r, _c = stack.pop()
                islands[_r][_c] = island_num
                for dr, dc in drc:
                    nr, nc = _r + dr, _c + dc
                    if (
                        not (0 <= nr < N and 0 <= nc < M)
                        or not arr[nr][nc]
                        or islands[nr][nc]
                    ):
                        continue

                    stack.append((nr, nc))

            island_num += 1

visited = [[False] * M for _ in range(N)]
bridges = [[999] * island_num for _ in range(island_num)]
edges = [set() for _ in range(island_num)]
for r in range(N):
    for c in range(M):
        if islands[r][c]:
            stack = [(r, c)]
            while stack:
                _r, _c = stack.pop()
                visited[_r][_c] = True
                for dr, dc in drc:
                    nr, nc = _r + dr, _c + dc
                    if not (0 <= nr < N and 0 <= nc < M) or visited[nr][nc]:
                        continue

                    if islands[nr][nc]:
                        stack.append((nr, nc))
                        continue

                    distance = 1
                    for i in range(1, max(N, M)):
                        nnr, nnc = nr + i * dr, nc + i * dc
                        if not (0 <= nnr < N and 0 <= nnc < M):
                            break

                        if islands[nnr][nnc] == islands[r][c]:
                            break

                        if islands[nnr][nnc] and islands[nnr][nnc] != islands[r][c]:
                            if distance > 1:
                                a, b = [islands[r][c], islands[nnr][nnc]]
                                bridges[a][b] = min(bridges[a][b], distance)
                                bridges[b][a] = min(bridges[b][a], distance)
                                edges[a].add(b)
                                edges[b].add(a)

                            break

                        distance += 1

check = set()
result = 0
que = [(0, 1)]
while que:
    distance, num = heappop(que)
    if num in check:
        continue
    check.add(num)
    result += distance
    for next_num in edges[num]:
        if not next_num in check:
            if bridges[num][next_num] == 999:
                continue

            heappush(que, (bridges[num][next_num], next_num))

if len(check) < island_num - 1:
    result = -1

print(result)
