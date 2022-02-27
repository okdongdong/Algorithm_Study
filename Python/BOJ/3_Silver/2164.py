# 카드2

N = int(input())

nums = list(range(2, N + 1, 2))
flag = True if N % 2 else False
while len(nums) > 1:
    temp = []
    for num in nums:
        if flag:
            temp.append(num)
        flag = not flag
    nums = temp

print(*nums) if nums else print(1)
