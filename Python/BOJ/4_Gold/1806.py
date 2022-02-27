# 부분합
N, S = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
num_sum = 0
min_len = N + 1

while right < N:
    if nums[right] >= S:
        min_len = 1
        break
    else:
        if num_sum < S:
            num_sum += nums[right]
            right += 1

        if num_sum >= S:
            num_sum -= nums[left]
            left += 1
            now_len = right - left + 1
            if now_len < min_len:
                min_len = now_len
else:
    while left < N:
        if num_sum < S:
            break
        num_sum -= nums[left]
        left += 1
        if num_sum < S:
            now_len = right - left + 1
            if now_len < min_len:
                min_len = now_len

if min_len > N:
    min_len = 0

print(min_len)
