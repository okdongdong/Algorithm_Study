import sys

sys.setrecursionlimit(int(10e6))

N, M = map(int, input().split())
board = [input() for _ in range(N)]
drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[False] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]


def dfs(r, c):
    if not (0 <= r < N and 0 <= c < M) or board[r][c] == "H":
        return 0

    if visited[r][c]:
        return -1

    if dp[r][c]:
        return dp[r][c]

    distance = int(board[r][c])
    visited[r][c] = True

    for dr, dc in drc:
        nr, nc = r + dr * distance, c + dc * distance

        cnt = dfs(nr, nc)

        if cnt == -1:
            return -1

        dp[r][c] = max(dp[r][c], cnt + 1)

    visited[r][c] = False

    return dp[r][c]


print(dfs(0, 0))
