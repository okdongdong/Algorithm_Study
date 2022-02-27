# 라면 사기 (Large)

N, B, C = map(int, input().split())
nums = list(map(int,input().split()))
total = 0
price1 = B
price2 = B + C
price3 = B + 2*C
if B > C:
    for i in range(N-2):
        if nums[i] == 0:
            continue

        if nums[i+1] > nums[i+2]: 
            min_num = min(nums[i],nums[i+1]-nums[i+2])
            total += min_num*price2
            nums[i] -= min_num
            nums[i+1] -= min_num

        min_num = min(nums[i:i+3])
        total += min_num*price3
        nums[i] -= min_num
        nums[i+1] -= min_num
        nums[i+2] -= min_num
        
    for i in range(N-1):
        if nums[i] == 0:
            continue
        
        min_num = min(nums[i:i+2])
        total += min_num*price2
        nums[i] -= min_num
        nums[i+1] -= min_num

    total += sum(nums)*price1

else:
    total = sum(nums)*B

print(total if total else 0)
