M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
drc = [(0, -1), (-1, 0), (0, 1), (1, 0)]

que = []

for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            que.append((r, c))

day = 0
while que:
    day += 1
    temp = []
    for r, c in que:
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M) or box[nr][nc]:
                continue

            box[nr][nc] = day
            temp.append((nr, nc))

    que = temp

for r in range(N):
    for c in range(M):
        if box[r][c] == 0:
            day = 0

print(day - 1)
