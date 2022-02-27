# 구간 합 구하기 3

import sys
import math
input = sys.stdin.readline


def update(x, y, c):
    val = table[x-1][y-1]
    table[x-1][y-1] = c
    x = (1 << level) + x - 1
    y = (1 << level) + y - 1
    while x > 0:
        temp_y = y
        while temp_y > 0:
            if tree[x][temp_y]:
                tree[x][temp_y] += c - val
            temp_y >>= 1
        x >>= 1


def cal1(x, y1, y2):
    temp = 0
    left = leaf_idx[y1-1]
    right = leaf_idx[y2-1]
    if left > right:
        right <<= 1

    if left >= 2*N:
        left >>= 1
        right >>= 1
    while left < right:
        if left % 2:
            temp += tree[x][left]
            left += 1
        if not right % 2:
            temp += tree[x][right]
            right -= 1
        left >>= 1
        right >>= 1

    if left == right:
        temp += tree[x][left]

    return temp


def cal2(x1, y1, x2, y2):
    temp = 0
    left = leaf_idx[x1-1]
    right = leaf_idx[x2-1]
    if left > right:
        right <<= 1
    if left >= 2*N:
        left >>= 1
        right >>= 1

    while left < right:
        if left % 2:
            temp += cal1(left, y1, y2)
            left += 1
        if not right % 2:
            temp += cal1(right, y1, y2)
            right -= 1
        left >>= 1
        right >>= 1

    if left == right:
        temp += cal1(left, y1, y2)

    return temp


N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
level = int(math.log2(N-1)) + 1 if N > 1 else 0
tree = [[0]*(1 << (level+1)) for _ in range(1 << (level+1))]
leaf_idx = [0]*N
for i in range(1 << level, (1 << level)+N):
    r = i if i < 2*N else i-N
    leaf_idx[i-(1 << level)] = r
    for j in range(1 << level, (1 << level)+N):
        c = j if j < 2*N else j-N
        tree[r][c] += table[i-(1 << level)][j-(1 << level)]
for i in range((1 << level)+N-1, N-1, -1):
    for j in range((1 << level)+N-1, 1, -1):
        tree[i][j >> 1] += tree[i][j]

for i in range((1 << level)+N-1, 1, -1):
    for j in range((1 << level)+N-1, 0, -1):
        tree[i >> 1][j] += tree[i][j]

result = []

for _ in range(M):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        update(*temp[1:])
    else:
        result.append(cal2(*temp[1:]))

print(*result, sep='\n')
