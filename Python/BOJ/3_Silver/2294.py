# 동전 2
n, k = map(int, input().split())
coins = set([int(input()) for _ in range(n)])
dp = [10001]*(k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[-1] if dp[-1] != 10001 else -1)
