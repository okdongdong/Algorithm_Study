# 백조의 호수
def cal_area(i):
    temp = [swan[i]]
    while temp:
        r, c = temp.pop()
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and not lake[nr][nc] and not board[nr][nc]:
                board[nr][nc] = i+1
                temp.append((nr, nc))


def date_cal():
    global stack
    date_cnt = 0
    while stack:
        temp = []
        date_cnt += 1
        for r, c in stack:
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if lake[nr][nc] == 'X':
                        lake[nr][nc] = lake[r][c] + 1
                        temp.append((nr, nc))

                    if not board[nr][nc]:
                        board[nr][nc] = board[r][c]

                    elif board[nr][nc] and board[r][c] and board[nr][nc] != board[r][c]:
                        return lake[nr][nc]

        temp2 = temp[:]
        while temp2:
            r, c = temp2.pop()
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if lake[nr][nc] != 'X' and board[r][c] and not board[nr][nc]:
                        board[nr][nc] = board[r][c]
                        temp2.append((nr, nc))

                    elif board[nr][nc] and board[r][c] and board[nr][nc] != board[r][c]:
                        return date_cnt

        stack = temp
    return date_cnt


R, C = map(int, input().split())
drc = [(0, 1), (0, -1), (-1, 0), (1, 0)]
lake = [list(input()) for _ in range(R)]
board = [[0]*C for _ in range(R)]
swan = []
stack = []
for r in range(R):
    for c in range(C):
        if lake[r][c] == '.':
            lake[r][c] = 0
            stack.append((r, c))
        elif lake[r][c] == 'L':
            lake[r][c] = 0
            stack.append((r, c))
            swan.append((r, c))
            board[r][c] = len(swan)

cal_area(0)
cal_area(1)

print(date_cal())
