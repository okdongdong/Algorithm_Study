# 1로 만들기 2
N = int(input())
nums = [9999]*(N+1)
edges = [0]*(N+1)
nums[0] = 0
nums[1] = 0

for i in range(1, N):
    if i*3 < N+1:
        if nums[i*3] > nums[i] + 1:
            nums[i*3] = nums[i] + 1
            edges[i*3] = i

    if i*2 < N+1:
        if nums[i*2] > nums[i] + 1:
            nums[i*2] = nums[i] + 1
            edges[i*2] = i

    if nums[i+1] > nums[i] + 1:
        nums[i+1] = nums[i] + 1
        edges[i+1] = i

cnt = nums[N]
result = []
i = N
while i > 0:
    result.append(i)
    i = edges[i]

print(nums[N])
print(*result)
