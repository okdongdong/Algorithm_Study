# RGB 거리
import sys
input = sys.stdin.readline

N = int(input())
houses_rgb = [list(map(int, input().split())) for _ in range(N)]

rgb = {0: (1, 2), 1: (0, 2), 2: (0, 1)}
min_val = 1000001
dp = [[0]*3 for _ in range(N)]

dp[0] = houses_rgb[0]
for i in range(1, N):

    for c, (c1, c2) in rgb.items():

        dp[i][c] = houses_rgb[i][c] + min(dp[i-1][c1], dp[i-1][c2])

print(min(dp[-1]))
