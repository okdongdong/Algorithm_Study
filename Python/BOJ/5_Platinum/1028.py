import sys
input = sys.stdin.readline

R, C = map(int, input().split())
mine = [input() for _ in range(R)]
direction1 = [[0]*C for _ in range(R)]
direction2 = [[0]*C for _ in range(R)]
direction3 = [[0]*C for _ in range(R)]
direction4 = [[0]*C for _ in range(R)]

# 좌하
for r in range(R):
    for c in range(C):
        if mine[r][c] == '1':
            if r == 0 or c == 0:
                direction1[r][c] = 1
            else:
                direction1[r][c] = direction1[r-1][c-1] + 1
# 우하
for r in range(R):
    for c in range(C-1, -1, -1):
        if mine[r][c] == '1':
            if r == 0 or c == C-1:
                direction2[r][c] = 1
            else:
                direction2[r][c] = direction2[r-1][c+1] + 1

# 좌상
for r in range(R-1, -1, -1):
    for c in range(C-1, -1, -1):
        if mine[r][c] == '1':
            if r == R-1 or c == C-1:
                direction3[r][c] = 1
            else:
                direction3[r][c] = direction3[r+1][c+1] + 1

# 우상
for r in range(R-1, -1, -1):
    for c in range(C):
        if mine[r][c] == '1':
            if r == R-1 or c == 0:
                direction4[r][c] = 1
            else:
                direction4[r][c] = direction4[r+1][c-1] + 1

max_size = 0
for r in range(R):
    for c in range(C):
        temp = max_size
        for size in range(temp, min(direction3[r][c], direction4[r][c])):
            r2 = r + size*2
            if r2 >= R:
                break
            if min(direction1[r2][c], direction2[r2][c]) >= size:
                max_size = max(max_size, size+1)

print(max_size)
