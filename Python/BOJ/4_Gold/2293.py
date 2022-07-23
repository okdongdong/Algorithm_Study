# 동전 1

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [0] * (K+1)
dp[0] = 1
coins = []

for _ in range(N):
    coin = int(input())
    coins.append(coin)

for coin in coins:
    for i in range(coin, K+1):

        dp[i] += dp[i-coin]

print(dp[K])
