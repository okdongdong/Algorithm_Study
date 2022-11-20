from heapq import heapify, heappop, heappush
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arr = [[0] * M for _ in range(N)]
arr[0][0] = 1
que = [(-board[0][0], 0, 0)]

while que:
    height, r, c = heappop(que)
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] >= board[r][c]:
            continue

        if not arr[nr][nc]:
            heappush(que, (-board[nr][nc], nr, nc))

        arr[nr][nc] += arr[r][c]

print(arr[-1][-1])
