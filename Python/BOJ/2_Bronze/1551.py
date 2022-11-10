N, K = map(int, input().split())
nums = list(map(int, input().split(",")))

for _ in range(K):
    temp = []

    for i in range(len(nums) - 1):
        temp.append(nums[i + 1] - nums[i])

    nums = temp

print(",".join(map(str, nums)))
