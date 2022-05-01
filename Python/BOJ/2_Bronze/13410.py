N, K = map(int, input().split())
nums = []

for i in range(1, K+1):
    nums.append(int(str(N*i)[::-1]))

print(max(nums))
