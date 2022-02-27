# 연구소 3

# 0: 빈칸, 1: 벽, 2: 바이러스를 놓을 수 있는 곳
# 4 <= N <= 50, 1 <= M <= 바이러스 총 개수 <= 10

import sys
input = sys.stdin.readline


def virus_move():
    global min_time_cnt

    stack = set()
    visited_rc = set()
    for i in range(len(virus)):
        if check[i]:
            stack.add(virus[i])
            visited_rc.add(virus[i])

    time_cnt = 0
    move_cnt = 0
    while stack:
        temp = set()
        time_cnt += 1
        if time_cnt > min_time_cnt:
            for r, c in visited_rc:    # 방문한 곳을 원상복구 해줌
                visited[r][c] = False
                if board[r][c] == 3:
                    board[r][c] = 0
            return

        # 바이러스가 다 퍼졌는지 확인
        if move_cnt == board_cnt:
            min_time_cnt = time_cnt
            for r, c in visited_rc:
                visited[r][c] = False
                if board[r][c] == 3:
                    board[r][c] = 0
            return

        for r, c, in stack:
            visited[r][c] = True
            for dr, dc in drc:
                nr = r+dr
                nc = c+dc
                # 0 또는 2일 경우 이동가능
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and not board[nr][nc] % 2:
                    temp.add((nr, nc))
                    visited_rc.add((nr, nc))
                    if not board[nr][nc]:
                        move_cnt += 1
                        board[nr][nc] = 3

        stack = temp

    for r, c in visited_rc:
        visited[r][c] = False
        if board[r][c] == 3:
            board[r][c] = 0


def select_virus(_start=0, _cnt=0):
    if _cnt == M:
        virus_move()
        return

    if len(virus) - _start < M - _cnt:  # 뽑을 수 있는 개수가 뽑아야 하는 개수보다 적으면 그냥 반환
        return

    for i in range(_start, len(virus)):
        check[i] = True
        select_virus(i+1, _cnt+1)
        check[i] = False


drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M = map(int, input().split())    # N: 연구소 크기, M: 놓을 수 있는 바이러스 수
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
virus = []
min_time_cnt = 948573832    # 시간체크
board_cnt = N**2    # 빈칸 개수 체크로 바이러스가 다 퍼졌는지 확인

for r in range(N):
    for c in range(N):
        if board[r][c]:
            board_cnt -= 1
            if board[r][c] == 2:
                virus.append((r, c))


check = [False] * len(virus)
select_virus()
print(-1 if min_time_cnt == 948573832 else min_time_cnt-1)
