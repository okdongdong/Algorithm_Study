import sys

input = sys.stdin.readline

N = int(input())
steps = [int(input()) for _ in range(N)] + [0]

dp = [0] * (N+1)
dp[0] = steps[0]
dp[1] = steps[0]+steps[1]

for i in range(2, N+1):
    dp[i] = max(dp[i-2], dp[i-3] + steps[i-1]) + steps[i]

print(dp[-2])
