N, T = map(int, input().split())
dp = [0] * (T + 1)

for i in range(N):
    K, S = map(int, input().split())
    for t in range(T, K - 1, -1):
        dp[t] = max(dp[t], dp[t - K] + S)

print(max(dp))
