# 용액

N = int(input())
nums = list(map(int, input().split()))
left = 0
right = N-1
min_sum = 9000000009
while left < right:
    now_sum = nums[left]+nums[right]
    if abs(now_sum) < min_sum:
        min_sum = abs(now_sum)
        result = [nums[left], nums[right]]

    if now_sum == 0:
        break

    elif now_sum > 0:
        right -= 1

    else:
        left += 1

print(*result)
