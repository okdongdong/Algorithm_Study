# 아기 상어 2
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

drc = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

que = []

for r in range(N):
    for c in range(M):
        if arr[r][c]:
            que.append((r, c))
cnt = 0
while que:
    cnt += 1
    temp = []

    for r, c in que:

        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if not(0 <= nr < N and 0 <= nc < M) or arr[nr][nc]:
                continue

            arr[nr][nc] = 1
            temp.append((nr, nc))

    que = temp

print(cnt-1)
