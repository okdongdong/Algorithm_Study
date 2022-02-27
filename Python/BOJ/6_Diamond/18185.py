# 라면 사기 (Small)

N = int(input())
nums = list(map(int,input().split()))
total = 0

for i in range(N-2):
    if nums[i] == 0:
        continue

    if nums[i+1] > nums[i+2]:   # 반례 1 2 1 1 처리
        min_num = min(nums[i],nums[i+1]-nums[i+2])
        total += min_num*5
        nums[i] -= min_num
        nums[i+1] -= min_num

    min_num = min(nums[i:i+3])
    total += min_num*7
    nums[i] -= min_num
    nums[i+1] -= min_num
    nums[i+2] -= min_num
    
for i in range(N-1):
    if nums[i] == 0:
        continue
    
    min_num = min(nums[i:i+2])
    total += min_num*5
    nums[i] -= min_num
    nums[i+1] -= min_num

total += sum(nums)*3

print(total if total else 0)