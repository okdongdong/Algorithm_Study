# 새로운 게임 2
import sys
input = sys.stdin.readline


def find_top(_num, top_list=[]):
    if horse_top[_num] == _num:
        return top_list+[_num]
    return find_top(horse_top[_num], top_list+[_num])


def is_4_or_more(_num, _cnt=1):
    if _cnt == 4:
        return True

    if horse_bottom[_num] == _num:
        return False

    return is_4_or_more(horse_bottom[_num], _cnt+1)


def move(_num, _r, _c, _color):
    global flag
    upper_list = find_top(_num)  # 현재 말와 그 위의 모든 말을 가져옴
    for upper in upper_list:    # 현재 말과 그 위의 모든 말 이동
        direction_r_c_list[upper][1] = _r
        direction_r_c_list[upper][2] = _c

    _horse_num = upper_list[0]
    top_horse = upper_list[-1]
    if _color == 1 and _horse_num != top_horse:
        for upper in upper_list:
            # 위아래 뒤집음
            horse_top[upper], horse_bottom[upper] = horse_bottom[upper], horse_top[upper]

        _horse_num = upper_list[-1]
        top_horse = upper_list[0]

    if horse_arr[_r][_c]:   # 기존에 있던 말 위로 올라갔을 때
        horse_top[horse_arr[_r][_c]] = _horse_num
        horse_bottom[_horse_num] = horse_arr[_r][_c]
    
    horse_arr[_r][_c] = top_horse
    if is_4_or_more(top_horse):
        flag = True


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direction_r_c_list = [0]
horse_arr = [[0]*N for _ in range(N)]
drc = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]
for horse_num in range(1, K+1):  # 위치, 방향정보 입력과 동시에 좌표 표시
    r, c, direction = map(int, input().split())
    r -= 1
    c -= 1
    horse_arr[r][c] = horse_num     # 좌표에 위치표시
    dr, dc = drc[direction]
    direction_r_c_list.append([(dr, dc), r, c])
flag = False
horse_top = list(range(K+1))
horse_bottom = list(range(K+1))
cnt = 0
while cnt < 1000:
    cnt += 1
    for horse_num in range(1, K+1):
        (dr, dc), r, c = direction_r_c_list[horse_num]
        nr = r+dr
        nc = c+dc
        # 범위밖 or 파란색
        if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
            nr = r-dr
            nc = c-dc
            direction_r_c_list[horse_num][0] = (-dr, -dc)
            # 또 범위밖 or 파란색
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                continue
        if horse_bottom[horse_num] != horse_num:
            horse_arr[r][c] = horse_bottom[horse_num]
            horse_top[horse_bottom[horse_num]] = horse_bottom[horse_num]
            horse_bottom[horse_num] = horse_num
        else:
            horse_arr[r][c] = 0
        move(horse_num, nr, nc, board[nr][nc])

    if flag:
        break
else:
    cnt = -1

print(cnt)
