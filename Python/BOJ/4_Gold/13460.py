# 구슬 탈출 2

def escape(R_now, B_now, cnt):
    global min_cnt
    if cnt >= min_cnt:    # 최소 반복횟수보다 작거나 같은 경우만 계산
        return
    # 시작 위치
    Rr, Rc = R_now
    Br, Bc = B_now

    for i in range(4):
        dr, dc = drc[i]
        flag_success, flag_fail = False, False
        nRr, nRc = Rr, Rc
        nBr, nBc = Br, Bc
        while True:
            # 빨간 공 이동
            if not flag_success and board[nRr + dr][nRc + dc] == '.' or board[nRr + dr][nRc + dc] == 'O':
                R_flag = True
                board[nRr][nRc] = '.'
                nRr += dr
                nRc += dc
                if board[nRr][nRc] == 'O':
                    flag_success = True
                else:
                    board[nRr][nRc] = 'R'
            else:
                R_flag = False

            # 파란 공 이동        
            if not flag_fail and board[nBr + dr][nBc + dc] == '.' or board[nBr + dr][nBc + dc] == 'O':
                board[nBr][nBc] = '.'
                B_flag = True
                nBr += dr
                nBc += dc
                if board[nBr][nBc] == 'O':
                    flag_fail = True
                else:
                    board[nBr][nBc] = 'B'
            else:
                B_flag = False

            if not (R_flag or B_flag):
                break

        # 도착 위치
        R_next = (nRr, nRc)
        B_next = (nBr, nBc)

        if R_now == R_next and B_now == B_next:     # 시작 위치와 도착 위치가 같으면 더이상 진행하지 않음
            continue

        if flag_success and not flag_fail:          # 파란공이 구멍에 들어가지 않고 빨간공만 들어갔을 때
            min_cnt = cnt

        if not flag_fail:                           # 파란공이 구멍에 들어가지 않은 경우에만 추가로 조작함      
            escape(R_next, B_next, cnt + 1)

        # 재귀에서 나온 후 복구
        board[nRr][nRc] = '.'
        board[nBr][nBc] = '.'
        board[Rr][Rc] = 'R'
        board[Br][Bc] = 'B'
        board[Or][Oc] = 'O'


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            R_now = (r, c)
        elif board[r][c] == 'B':
            B_now = (r, c)
        elif board[r][c] == 'O':
            Or, Oc = r, c
min_cnt = 11
escape(R_now, B_now, 1)
print(min_cnt if min_cnt < 11 else -1)
