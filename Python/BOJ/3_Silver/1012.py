# 유기농 배추

import sys
input = sys.stdin.readline
dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
T = int(input())
result = []
for _ in range(T):
    M, N, K = map(int, input().split())  # 가로, 세로, 수
    x_y_list = [list(map(int, input().split()))for _ in range(K)]
    board = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for x, y in x_y_list:
        board[y][x] = 1

    for x in range(M):
        for y in range(N):
            if visited[y][x] or not board[y][x]:
                continue
            cnt += 1
            stack = [(x, y)]
            while stack:
                _x, _y = stack.pop()
                visited[_y][_x] = True
                for dx, dy in dxy:
                    nx = _x+dx
                    ny = _y+dy
                    if 0 <= nx < M and 0 <= ny < N and board[ny][nx] and not visited[ny][nx]:
                        stack.append((nx, ny))
    
    result.append(str(cnt))
print('\n'.join(result))
