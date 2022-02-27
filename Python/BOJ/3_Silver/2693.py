T = int(input())

result = []
for _ in range(T):
    nums = list(map(int, input().split()))
    result.append(sorted(nums, reverse=True)[2])

print(*result, sep='\n')
