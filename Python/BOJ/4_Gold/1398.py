# 동전 문제
T = int(input())

# 1, 10, 25구간만 dp필요
dp = [0]*100
for i in range(1, 100):
    if i < 10:
        dp[i] = dp[i-1] + 1
    elif i < 25:
        dp[i] = min(dp[i-1], dp[i-10]) + 1
    else:
        dp[i] = min(dp[i-1], dp[i-10], dp[i-25]) + 1

result = []
for _ in range(T):
    num = int(input())
    cnt = 0
    while num:
        num, idx = divmod(num, 100)
        cnt += dp[idx]

    result.append(cnt)

print(*result, sep='\n')
