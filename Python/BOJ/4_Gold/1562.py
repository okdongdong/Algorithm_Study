# 계단 수
N = int(input())
stair_nums = [0]*101
stair_nums[10] = 1

for i in range(11,N):
    stair_nums[i] = stair_nums[i-1]*2+stair_nums[i-2]

