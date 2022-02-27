# 행렬 곱셈 순서

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

dp = [[987987987]*(N+1) for _ in range(N+1)]

for i in range(N):
    dp[1][i] = 0

for i in range(N-1):
    dp[2][i] = nums[i][0]*nums[i][1]*nums[i+1][1]

for cnt in range(3, N+1):
    for start_num in range(N-cnt+1):
        for left in range(1, cnt):
            right = cnt-left
            now_sum = dp[left][start_num] + dp[right][start_num + left] + (nums[0][0] * nums[left-1][1] * nums[cnt-1][1])
            if dp[cnt][start_num] > now_sum:
                dp[cnt][start_num] = now_sum

print(dp[-1][0])
