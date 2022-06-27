max_num = (0, 0, 0)
for i in range(9):
    nums = list(map(int, input().split()))
    for j in range(9):
        max_num = max(max_num, (nums[j], i+1, j+1))

print(max_num[0])
print(max_num[1], max_num[2])
