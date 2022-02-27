# 오아시스 재결합
import sys
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
result = 0
stack = []
for j in range(N):
    i = len(stack) - 1
    while stack and i >= 0:
        result += 1
        # 작을 때
        if nums[j] > stack[i]:
            stack.pop()
            i -= 1

        # 같을 때
        elif nums[j]==stack[i]:
            i -= 1

        # 클 때
        elif nums[j] < stack[i]:
            break

    stack.append(nums[j])

print(result)
