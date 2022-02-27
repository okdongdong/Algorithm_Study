# 숫자 카드
N = int(input())
cards = set(map(int, input().split()))
M = int(input())
nums = map(int, input().split())
result = []
for num in nums:
    result.append('1' if num in cards else '0')

print(' '.join(result))
