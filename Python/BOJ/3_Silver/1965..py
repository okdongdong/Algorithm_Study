# 상자넣기

N = int(input())
nums = list(map(int, input().split()))

dp = [(1, nums[i]) for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if nums[i] > dp[j][1]:
            dp[i] = sorted((dp[i], (dp[j][0] + 1, nums[i])),
                           key=lambda x: (-x[0], x[1]))[0]

print(max(dp)[0])
