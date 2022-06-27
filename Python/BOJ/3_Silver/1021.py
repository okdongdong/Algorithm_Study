from collections import deque

N, M = map(int, input().split())
idx_list = list(map(int, input().split()))
nums = deque(range(1, N+1))
result = 0

for idx in idx_list:
    temp_cnt = 0
    while nums[0] != idx:
        temp_cnt += 1
        nums.rotate()

    nums.popleft()
    result += min(temp_cnt, N-temp_cnt)
    N -= 1

print(result)
