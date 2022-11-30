import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

result = (float("inf"), 0)
for height in range(257):
    cost = 0
    block_cnt = B

    for r in range(N):
        for c in range(M):
            diff = board[r][c] - height
            cost += 2 * diff if diff > 0 else -diff
            block_cnt += diff

    if block_cnt < 0:
        continue
    result = min(result, (cost, height), key=lambda x: (x[0], -x[1]))

print(*result)
