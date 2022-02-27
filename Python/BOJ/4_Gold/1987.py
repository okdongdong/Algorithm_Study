# 알파벳

import sys
input = sys.stdin.readline

def move(_r, _c, cnt):
    global max_move

    visited_alpha[board[_r][_c]] = True
    visited[_r][_c] = True

    if max_move < cnt:
        max_move = cnt

    for dr, dc in drc:
        nr = _r + dr
        nc = _c + dc
        if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
            if visited_alpha[board[nr][nc]]:
                continue
            move(nr, nc, cnt+1)
    
    visited_alpha[board[_r][_c]] = False
    visited[_r][_c] = False

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
visited_alpha = [False]*26
max_move = 0
drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

move(0, 0, 1)

print(max_move)