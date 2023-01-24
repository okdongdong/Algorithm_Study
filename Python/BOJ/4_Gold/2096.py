import sys

input = sys.stdin.readline

N = int(input())
dp1 = list(map(int, input().split()))
dp2 = dp1[:]

for _ in range(N - 1):
    a, b, c = map(int, input().split())

    dp = dp1[:]
    dp1[0] = max(dp[0], dp[1]) + a
    dp1[1] = max(dp[0], dp[1], dp[2]) + b
    dp1[2] = max(dp[1], dp[2]) + c

    dp = dp2[:]
    dp2[0] = min(dp[0], dp[1]) + a
    dp2[1] = min(dp[0], dp[1], dp[2]) + b
    dp2[2] = min(dp[1], dp[2]) + c

print(max(dp1), min(dp2))
