import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[0]*M for _ in range(N)]
visited[0][0] = 2
que = [(0, 0)]
min_cnt = 1000000
cnt = 0

while que:
    cnt += 1
    temp = []
    for r, c in que:
        if r == N-1 and c == M-1:
            min_cnt = cnt
            break

        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] < visited[r][c] and arr[nr][nc] == '0':
                    temp.append((nr, nc))
                    visited[nr][nc] = visited[r][c]

                elif visited[r][c] > 1 and arr[nr][nc] == '1':
                    temp.append((nr, nc))
                    visited[nr][nc] = visited[r][c] - 1

    else:
        que = temp
        continue

    break


print(min_cnt if min_cnt < 1000000 else -1)
