# N-Queen

def board_check(r, c, e):
    for dr, dc in drc:
        for i in range(1, N):
            nr, nc = r+dr*i, c+dc*i

            if not (0 <= nr < N and 0 <= nc < N):
                break

            board[nr][nc] += e


def recur(r):
    global cnt

    if r == N:
        cnt += 1
        return

    for c in range(N):
        if check[c] or board[r][c]:
            continue

        board_check(r, c, 1)
        check[c] = True

        recur(r+1)

        board_check(r, c, -1)
        check[c] = False


N = int(input())
cnt = 0
drc = [(1, 1), (1, -1)]
check = [False] * N
board = [[0] * N for _ in range(N)]

recur(0)

print(cnt)
