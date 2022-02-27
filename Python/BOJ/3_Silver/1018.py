# 체스판 다시 칠하기
def board_check(_r, _c, weight):
    _cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j+weight) % 2 and board[_r+i][_c+j] == 'W':
                _cnt += 1
            elif (i+j+weight) % 2 == 0 and board[_r+i][_c+j] == 'B':
                _cnt += 1
        if _cnt > min_cnt:
            return min_cnt
    return _cnt


M, N = map(int, input().split())
board = [input() for _ in range(M)]
min_cnt = M * N
for r in range(M-7):
    for c in range(N-7):
        cnt1 = board_check(r, c, 1)
        cnt2 = board_check(r, c, 2)
        cnt = min(cnt1, cnt2)
        if cnt < min_cnt:
            min_cnt = cnt

print(min_cnt)
