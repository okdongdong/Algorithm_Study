# 아기 상어
def shark_move(_r, _c):
    global fish
    stack = set([(_r, _c)])
    visited_check = []
    target_rc = 0
    _cnt = 0
    while stack:
        temp = set()
        _cnt += 1
        for _r, _c in stack:
            visited[_r][_c] = True
            visited_check.append((_r, _c))

            for dr, dc in drc:
                nr = _r+dr
                nc = _c+dc
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] <= shark_body and not visited[nr][nc]:
                    temp.add((nr, nc))
                    if board[nr][nc] and board[nr][nc] < shark_body:
                        if target_rc:
                            tr, tc = target_rc
                            if nr < tr or (nr == tr and nc < tc):
                                target_rc = nr, nc

                        else:
                            target_rc = nr, nc

        if target_rc:
            tr, tc = target_rc
            board[tr][tc] = 0
            for _r, _c in visited_check:
                visited[_r][_c] = False
            return tr, tc, _cnt

        stack = temp

    return False    # 먹을 수 있는 물고기가 없을 때


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 상좌우하
visited = [[False]*N for _ in range(N)]
fish = [set() for _ in range(7)]
total_time = 0
shark_body = 2
eat_cnt = 0

for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            visited[r][c] = True
            board[r][c] = 0
            shark_r, shark_c = r, c
            break
    if visited[r][c]:
        break

while True:

    try:
        shark_r, shark_c, cnt = shark_move(shark_r, shark_c)
        total_time += cnt
        eat_cnt += 1
        if eat_cnt == shark_body and shark_body < 7:
            shark_body += 1
            eat_cnt = 0

    except:
        break

print(total_time)
