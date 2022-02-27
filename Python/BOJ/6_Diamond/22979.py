# 색종이 붙이기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
paper = [input().rstrip() for _ in range(N)]
pre_check = [[1] * M for _ in range(N)]

# 가로방향 최소길이
min_length_c = M
for r in range(N):
    cnt = 0
    for c in range(M):
        if paper[r][c] == '#':
            pre_check[r][c] = 0
            if cnt and min_length_c > cnt:
                min_length_c = cnt
            cnt = 0
        else:
            cnt += 1
    if cnt and min_length_c > cnt:
        min_length_c = cnt

# 세로방향 최소길이
min_length_r = N
for c in range(M):
    cnt = 0
    for r in range(N):
        if paper[r][c] == '#':
            if cnt and min_length_r > cnt:
                min_length_r = cnt
            cnt = 0
        else:
            cnt += 1
    if cnt and min_length_r > cnt:
        min_length_r = cnt

cnt = 1  # 색종이 종류의 수
for n in range(1, min_length_r + 1):
    for m in range(1, min_length_c + 1):
        if n == 1 and m == 1:
            continue

        check = [pre_check[i][:] for i in range(N)]
        for sr in range(N - n + 1):
            sc = 0
            while sc < M - m + 1:
                flag = True
                for r in range(n):
                    for c in range(m):
                        if paper[sr + r][sc + c] == '#':
                            dc = c
                            flag = False

                    if not flag:
                        break
                if flag:
                    for r in range(n):
                        for c in range(m):
                            check[sr + r][sc + c] = 0
                else:
                    sc += dc
                sc += 1

            if sum(check[sr]):
                break
        else:
            for r in range(N - n + 1, N):
                if sum(check[r]):
                    break
            else:
                cnt += 1
print(cnt)
