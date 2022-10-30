# 포도주
N = int(input())
포도주 = [int(input()) for _ in range(N)]

if N < 3:
    print(sum(포도주))

else:
    dp = [0] * N
    dp[0] = 포도주[0]
    dp[1] = 포도주[0] + 포도주[1]
    dp[2] = max(포도주[0] + 포도주[2], 포도주[1] + 포도주[2], dp[1])

    for i in range(3, N):
        dp[i] = max(dp[i - 3] + 포도주[i - 1] + 포도주[i], dp[i - 2] + 포도주[i], dp[i - 1])

    print(dp[-1])
