# 좋다
N = int(input())
nums = list(map(int, input().split()))
nums_dict = {}

for num in nums:
    if nums_dict.get(num):
        nums_dict[num] += 1
    else:
        nums_dict[num] = 1


nums_set = set(nums_dict.keys())

cnt = 0

for i in range(N):
    num = nums[i]
    for j in range(N):
        if i == j:
            continue

        num2 = nums[j]

        if (num - num2) in nums_set:
            if num == num2 and nums_dict[num] < 3:
                continue

            if num - num2 == num and nums_dict[num] < 2:
                continue

            if num - num2 == num2 and nums_dict[num2] < 2:
                continue

            cnt += 1
            break

print(cnt)
