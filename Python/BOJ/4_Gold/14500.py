# 테트로미노

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

# 2X3 직사각형에 대하여 적용    
for r in range(N - 2):
    for c in range(M - 1):
        paper_sum = 0
        nums = []
        for i in range(3):
            for j in range(2):
                paper_sum += paper[r + i][c + j]
                nums.append((paper[r + i][c + j], i, j))

        for i in range(5):
            for j in range(i + 1, 6):
                if nums[i][1] == 1 and nums[j][1] == 1:
                    continue
                elif abs(nums[i][1] - nums[j][1]) == 1 and abs(nums[i][2] - nums[j][2]) == 1:
                    continue

                now_sum = paper_sum - nums[i][0] - nums[j][0]
                if max_sum < now_sum:
                    max_sum = now_sum

# 3X2 직사각형에 대하여 적용    
for r in range(N - 1):
    for c in range(M - 2):
        paper_sum = 0
        nums = []
        for i in range(2):
            for j in range(3):
                paper_sum += paper[r + i][c + j]
                nums.append((paper[r + i][c + j], i, j))

        for i in range(5):
            for j in range(i + 1, 6):
                if nums[i][2] == 1 and nums[j][2] == 1:
                    continue
                elif abs(nums[i][1] - nums[j][1]) == 1 and abs(nums[i][2] - nums[j][2]) == 1:
                    continue

                now_sum = paper_sum - nums[i][0] - nums[j][0]
                if max_sum < now_sum:
                    max_sum = now_sum

# 1X4
for r in range(N - 3):
    for c in range(M):
        now_sum = 0
        for i in range(4):
            now_sum += paper[r + i][c]
        if max_sum < now_sum:
            max_sum = now_sum

# 4X1
for r in range(N):
    for c in range(M - 3):
        now_sum = 0
        for i in range(4):
            now_sum += paper[r][c + i]
        if max_sum < now_sum:
            max_sum = now_sum

print(max_sum)

# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1000
