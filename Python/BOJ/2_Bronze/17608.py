# 막대기
import sys
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
now_max = 0
cnt = 0
for i in range(N-1, -1, -1):

    if now_max < nums[i]:
        cnt += 1
        now_max = nums[i]

print(cnt)
