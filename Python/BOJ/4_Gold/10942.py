# 팰린드롬?
import sys
input = sys.stdin.readline

N = int(input())
nums = input().split()
pal = [['0']*(N+1) for _ in range(N+1)]

# 홀수개
for i in range(N):
    left, right = i, i
    while left >= 0 and right < N:
        if nums[left] != nums[right]:
            break
        pal[left+1][right+1] = '1'
        left -= 1
        right += 1

# 짝수개
for i in range(N-1):
    left, right = i, i+1
    while left >= 0 and right < N:
        if nums[left] != nums[right]:
            break
        pal[left+1][right+1] = '1'
        left -= 1
        right += 1

result = []
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    result.append(pal[a][b])

print('\n'.join(result))
