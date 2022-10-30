N = int(input())
nums = list(map(int, input().split()))

dp = [(1, nums[i], -1) for i in range(N)]  # cnt, val, idx
dp[0] = (1, nums[0], -1)

for i in range(N):
    for j in range(i):
        if nums[i] > dp[j][1]:
            dp[i] = max((dp[j][0] + 1, nums[i], j), dp[i])

length, val, idx = max(dp)
result = [val]

while idx > -1:
    result.append(dp[idx][1])
    idx = dp[idx][2]

print(length)
print(*result[::-1])
