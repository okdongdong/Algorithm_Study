# 어항 정리

def check_rc(c):
    r_cnt = 0
    for _r in range(N-1, -1, -1):
        if board[_r][c] == -1:
            break
        r_cnt += 1

    c_cnt = 0
    for _c in range(c, N):
        if board[-2][_c] == -1:
            break
        c_cnt += 1

    return r_cnt, c_cnt


def rotate(c, r_cnt, c_cnt):
    if c + c_cnt + r_cnt <= N:
        arr = [[0]*r_cnt for _ in range(c_cnt)]
        for _r in range(r_cnt):
            for _c in range(c_cnt):
                arr[_c][_r] = board[N-1-_r][c+_c]
                board[N-1-_r][c+_c] = -1

        for _r in range(r_cnt):
            for _c in range(c_cnt):
                board[N-1-c_cnt + _c][c+c_cnt+_r] = arr[_c][_r]

    return c+c_cnt, r_cnt


def move_fish():
    diff = set()
    for c in range(N):
        for r in range(N-1, -1, -1):
            if board[r][c] == -1:
                break
            for dr, dc in drc:
                nr = r+dr
                nc = c+dc
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] != -1:
                    if board[nr][nc] > board[r][c]:
                        r1, c1 = nr, nc
                        r2, c2 = r, c
                        d = (board[nr][nc] - board[r][c])//5
                    else:
                        r1, c1 = r, c
                        r2, c2 = nr, nc
                        d = (board[r][c] - board[nr][nc])//5

                    if d:
                        diff.add((r1, c1, r2, c2, d))

    for r1, c1, r2, c2, d in diff:
        board[r1][c1] -= d
        board[r2][c2] += d


N, K = map(int, input().split())
fishes = list(map(int, input().split()))
board = [[-1]*N for _ in range(N)]
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    board[-1][i] = fishes[i]
cnt = 1
while True:
    # 최소인 곳에 +1 해줌
    min_fish = min(board[-1])
    for i in range(N):
        if board[-1][i] == min_fish:
            board[-1][i] += 1

    board[-2][1] = board[-1][0]
    board[-1][0] = -1

    # 돌돌돌..
    c = 1
    r_cnt = 0
    while c + r_cnt <= N:
        c, r_cnt = rotate(c, *check_rc(c))

    move_fish()

    # 2단계 쌓기
    temp = []
    for c in range(N):
        for r in range(N-1, -1, -1):
            if board[r][c] == -1:
                break

            temp.append(board[r][c])
            board[r][c] = -1

    for r in [-1, -4, -3, -2]:
        for c in range(N-1, N-1-N//4, -1):
            if r % 2:
                board[r][c] = temp.pop()
            else:
                board[r][7*(N//4)-1-c] = temp.pop()

    move_fish()

    # 다시펴기
    temp = []
    for c in range(N):
        for r in range(N-1, -1, -1):
            if board[r][c] == -1:
                break

            temp.append(board[r][c])
            board[r][c] = -1

    if max(temp) - min(temp) <= K:
        break

    for c in range(N-1, -1, -1):
        board[-1][c] = temp.pop()

    cnt += 1

print(cnt)
