# 원판 돌리기
import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())

boards = [deque()] + [deque(map(int, input().split())) for _ in range(N)]
x_d_k_list = [list(map(int, input().split())) for _ in range(T)]
clean_board = [False]*(N+1)
# d == 0 시계방향, d == 1 반시계방향
for x, d, k in x_d_k_list:
    for i in range(x, N+1, x):
        if clean_board[i]:
            continue
        if d:
            for _ in range(k):
                boards[i].append(boards[i].popleft())
        else:
            for _ in range(k):
                boards[i].appendleft(boards[i].pop())

    clear_list = set()
    nums = [0]*1001
    for i in range(1, N+1):
        if clean_board[i]:
            continue
        for j in range(M):
            if not boards[i][j]:
                continue
            j2 = (j+1) % M
            j3 = (j-1) % M
            if i < N and boards[i][j] == boards[i+1][j]:
                clear_list.add((i, j))
                clear_list.add((i+1, j))
            if boards[i][j] == boards[i][j2]:
                clear_list.add((i, j))
                clear_list.add((i, j2))
            if boards[i][j] == boards[i][j3]:
                clear_list.add((i, j))
                clear_list.add((i, j3))

    for i, j in clear_list:
        boards[i][j] = 0

    cnt = 0
    temp_sum = 0
    ij_list = []

    for i in range(1, N+1):
        if clean_board[i]:
            continue
        pre_cnt = cnt
        for j in range(M):
            if boards[i][j]:
                ij_list.append((i, j))
                temp_sum += boards[i][j]
                cnt += 1
        if pre_cnt == cnt:
            clean_board[i] = True

    if cnt and not clear_list:
        avg = temp_sum / cnt
        for i, j in ij_list:
            if boards[i][j]:
                if boards[i][j] > avg:
                    boards[i][j] -= 1
                elif boards[i][j] < avg:
                    boards[i][j] += 1

print(sum(map(sum, boards)))
