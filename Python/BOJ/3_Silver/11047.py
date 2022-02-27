# 동전 0

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

cnt = 0
while K:
    coin = coins.pop()
    cnt += K//coin
    K %= coin

print(cnt)
