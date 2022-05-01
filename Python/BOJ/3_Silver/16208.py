# 귀찮음

from collections import deque

N = int(input())
nums = deque(map(int, input().split()))

cost = 0
while len(nums) > 1:
    a = nums.popleft()
    b = nums.popleft()

    cost += a*b
    nums.append(a+b)

print(cost)
