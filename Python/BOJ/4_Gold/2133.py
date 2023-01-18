N = int(input())
dp = [0] * 31
dp[0] = 1
dp[2] = 3

for i in range(4, N + 1, 2):
    dp[i] = dp[i - 2] * 4 - dp[i - 4]

print(dp[N])
