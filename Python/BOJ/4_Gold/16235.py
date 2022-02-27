# 나무 재테크
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

area = [[5]*N for _ in range(N)]
area_add = [list(map(int, input().split())) for _ in range(N)]

trees = [list(map(int, input().split())) for _ in range(M)]
trees_trees = [[[] for _ in range(N)] for _ in range(N)]
for r, c, age in trees:
    trees_trees[r-1][c-1].append(age)

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]
reproduce_list = []
for _ in range(K):

    # 봄 & 여름
    for r in range(N):
        for c in range(N):
            if not trees_trees[r][c]:
                continue

            nutrient = 0    
            for i in range(len(trees_trees[r][c])-1, -1, -1):
                age = trees_trees[r][c][i]
                if area[r][c] >= age:
                    area[r][c] -= age
                    trees_trees[r][c][i] += 1
                    if (age+1) % 5 == 0:
                        reproduce_list.append((r, c))
                else:
                    for j in range(0, i+1):
                        nutrient += age//2
                        age = trees_trees[r][c][j]
                    trees_trees[r][c] = trees_trees[r][c][i+1:]
                    break
            area[r][c] += nutrient
    
    # 가을
    while reproduce_list:
        r, c = reproduce_list.pop()
        for dr, dc in directions:
            if 0 <= r+dr < N and 0 <= c+dc < N:
                trees_trees[r+dr][c+dc].append(1)

    # 겨울
    for r in range(N):
        for c in range(N):
            area[r][c] += area_add[r][c]

result = 0
for r in range(N):
    for c in range(N):
        result += len(trees_trees[r][c])

print(result)
