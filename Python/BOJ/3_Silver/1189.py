# 컴백홈


R, C, K = map(int, input().split())
arr = [input() for _ in range(R)]

drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False]*C for _ in range(R)]
visited[R-1][0] = True
cnt = 0


def dfs(r=R-1, c=0, move_cnt=0):
    global cnt

    if move_cnt == K-1 and (r, c) == (0, C-1):
        cnt += 1
        return

    if move_cnt >= K-1:
        return

    for dr, dc in drc:
        nr, nc = r+dr, c+dc
        if not(0 <= nr < R and 0 <= nc < C):
            continue

        if visited[nr][nc] or arr[nr][nc] == 'T':
            continue

        visited[nr][nc] = True
        dfs(nr, nc, move_cnt+1)

        visited[nr][nc] = False


dfs()
print(cnt)
