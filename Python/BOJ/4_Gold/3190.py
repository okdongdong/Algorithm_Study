# 뱀

import sys,pprint

input = sys.stdin.readline

N = int(input())  # 보드의 크기
K = int(input())  # 사과의 개수
apples = [list(map(int, input().split())) for _ in range(K)]  # 사과의 좌표

L = int(input())                                    # 방향전환 횟수
moves = [input().split() for _ in range(L)]         # 시간, 뱀의 방향전환
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]      # 우하좌상
board = [[1] * (N + 1) for _ in range(N + 1)]       # 좌상단 == (1,1)

for r, c in apples:             # 사과의 위치 표시
    board[r][c] = 2

snake_body = [(1, 1)]           # 뱀의 위치 좌표
head, tail = 0, 0
move_idx = 0
move_direction = 0              # 뱀의 시작 방향
game_time = 0                   # 게임 시간

hr, hc = snake_body[head]       # 머리의 위치
while True:
    game_time += 1
    dr, dc = direction[move_direction]
    snake_body.append((hr + dr, hc + dc))
    head += 1                   # 앞으로 한칸 전진
    hr, hc = snake_body[head]   # 머리의 위치
    tr, tc = snake_body[tail]   # 꼬리의 위치

    # 0: 뱀, 1: 빈칸, 2: 사과
    if 0 < hr <= N and 0 < hc <= N and board[hr][hc]:
        if board[hr][hc] == 1:
            board[tr][tc] = 1
            tail += 1
        board[hr][hc] = 0
    else:
        break

    if move_idx < L and int(moves[move_idx][0]) == game_time:
        if moves[move_idx][1] == 'D':
            move_direction = (move_direction + 1) % 4
        else:
            move_direction = (move_direction + 3) % 4
        move_idx += 1

print(game_time)
pprint.pprint(board)