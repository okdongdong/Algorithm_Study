# 1, 2, 3 더하기
T = int(input())

dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(T):
    N = int(input())
    if not dp[N]:
        for i in range(3, N+1):
            if dp[i]:
                continue
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])
