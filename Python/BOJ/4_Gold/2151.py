from collections import deque


N = int(input())
arr = [list(input()) for _ in range(N)]
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_door():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "#":
                return r, c


r, c = get_door()
arr[r][c] = "*"
visited = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
que = deque([(r, c, d) for d in range(4)])

while que:
    r, c, d = que.popleft()

    for di, (dr, dc) in enumerate(drc):
        if (d + 2) % 4 == di:
            continue

        for i in range(1, N):
            nr, nc = r + dr * i, c + dc * i
            if not (0 <= nr < N and 0 <= nc < N) or arr[nr][nc] == "*":
                break

            for nd in [(di + 1) % 4, (di - 1) % 4]:
                if visited[nr][nc][nd] > -1 or arr[nr][nc] == ".":
                    continue

                visited[nr][nc][nd] = visited[r][c][di] + 1
                que.append((nr, nc, nd))

r, c = get_door()
print(min(set(visited[r][c]) - {-1}))
