import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[[0] * H for _ in range(M)] for _ in range(N)]
drch = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
que = []
for h in range(H):
    for r in range(N):
        temp = list(map(int, input().split()))
        for c in range(M):
            box[r][c][h] = temp[c]
            if box[r][c][h] == 1:
                que.append((r, c, h))

cnt = -1
while que:
    temp = []
    cnt += 1
    for r, c, h in que:
        for dr, dc, dh in drch:
            nr, nc, nh = r + dr, c + dc, h + dh
            if not (0 <= nr < N and 0 <= nc < M and 0 <= nh < H) or box[nr][nc][nh]:
                continue

            temp.append((nr, nc, nh))
            box[nr][nc][nh] = 1

    que = temp

for r in range(N):
    for c in range(M):
        for h in range(H):
            if box[r][c][h] == 0:
                cnt = -1

print(cnt)
