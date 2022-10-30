# 오아시스 재결합
import sys

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
result = 0
stack = []
for i in range(N):
    while stack and stack[-1][0] < nums[i]:
        num, cnt = stack.pop()
        result += cnt

    if not stack:
        stack.append([nums[i], 1])
        continue

    if stack[-1][0] == nums[i]:
        num, cnt = stack.pop()
        result += cnt + bool(stack)
        stack.append([nums[i], cnt + 1])

    else:
        result += 1
        stack.append([nums[i], 1])

print(result)
