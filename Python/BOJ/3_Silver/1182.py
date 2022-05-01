from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

for i in range(1, N+1):
    sub_nums_list = combinations(nums, i)
    for sub_nums in sub_nums_list:
        if sum(sub_nums) == S:
            cnt += 1

print(cnt)
