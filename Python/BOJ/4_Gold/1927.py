from heapq import heappush, heappop
import sys

input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    temp_num = int(input())
    if temp_num:
        heappush(nums, temp_num)
        continue

    if nums:
        print(heappop(nums))

    else:
        print(0)
