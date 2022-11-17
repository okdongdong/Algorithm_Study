import sys

input = sys.stdin.readline

K, N = map(int, input().split())
nums = [input().rstrip() for _ in range(K)]

selected = nums[:]
max_num = max(nums, key=lambda x: (len(x), x))
selected += [max_num] * (N - K)

selected.sort(reverse=True, key=lambda x: (x * 10))

print("".join(selected))
