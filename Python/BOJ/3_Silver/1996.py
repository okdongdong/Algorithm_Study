# 지뢰 찾기
import sys
input = sys.stdin.readline

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
N = int(input())
mine_arr = [input() for _ in range(N)]
result_arr = [[0]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if mine_arr[r][c] == '.':
            continue
        result_arr[r][c] = '*'
        for i in range(8):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < N and 0 <= nc < N and mine_arr[nr][nc] == '.':
                result_arr[nr][nc] += int(mine_arr[r][c])

for r in range(N):
    print(''.join(map(lambda x: 'M' if x != '*' and x >= 10 else str(x), result_arr[r])))
