# 파이프 옮기기 1

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt_arr = [[[0, 0, 0] for _ in range(N)] for _ in range(N)] # [가로, 세로, 대각]
r, c = 0, 1
cnt_arr[r][c-1][0] = 1
cnt_arr[r][c][0] = 1

for r in range(N):
    for c in range(2, N):
        if board[r][c] != 1:
            if 0 <= r < N and 1 <= c < N:
                cnt_arr[r][c][0] += cnt_arr[r][c-1][0] + cnt_arr[r][c-1][2]

            if 1 <= r < N and 0 <= c < N:
                cnt_arr[r][c][1] += cnt_arr[r-1][c][1] + cnt_arr[r-1][c][2]

            if 1 <= r < N and 1 <= c < N and board[r-1][c] != 1 and board[r][c-1] != 1:
                cnt_arr[r][c][2] += sum(cnt_arr[r-1][c-1])

print(sum(cnt_arr[-1][-1]))
