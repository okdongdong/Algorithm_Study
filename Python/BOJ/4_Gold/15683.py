# 감시
def view_check(_r, _c, _direction, check=-1):
    global blind_area_cnt
    dr, dc = drc[_direction]

    for mult in range(1, 8):   # N,M 의 최대범위가 8
        nr = _r + dr*mult
        nc = _c + dc*mult
        if not (0 <= nr < N and 0 <= nc < M) or office[nr][nc] == 6:
            return

        if office[nr][nc] > 0:
            continue
        elif office[nr][nc] == 0:
            blind_area_cnt += check

        office[nr][nc] += check

        if office[nr][nc] == 0:
            blind_area_cnt += check


def camera_view(_i=0):
    global min_blind_cnt
    if _i == len(CCTVs):
        if blind_area_cnt < min_blind_cnt:
            min_blind_cnt = blind_area_cnt
        return 

    _r, _c, _CCTV_num = CCTVs[_i]
    if _CCTV_num == 1:
        for _direction in range(4):
            view_check(_r, _c, _direction)

            camera_view(_i + 1)

            view_check(_r, _c, _direction, 1)

    elif _CCTV_num == 2:
        for _direction in range(2):
            _direction2 = (_direction + 2) % 4
            view_check(_r, _c, _direction)
            view_check(_r, _c, _direction2)

            camera_view(_i + 1)

            view_check(_r, _c, _direction, 1)
            view_check(_r, _c, _direction2, 1)

    elif _CCTV_num == 3:
        _direction = 0
        for i in range(2):
            _direction2 = (_direction+i) % 4
            view_check(_r, _c, _direction2)

        camera_view(_i + 1)

        for i in range(3):
            _direction2 = (i+2) % 4
            view_check(_r, _c, i, 1)
            view_check(_r, _c, _direction2)
            camera_view(_i + 1)

        _direction = -1
        for i in range(2):
            _direction2 = (_direction+i) % 4
            view_check(_r, _c, _direction2, 1)

    elif _CCTV_num == 4:
        _direction = 0

        for i in range(3):
            _direction2 = (_direction+i) % 4
            view_check(_r, _c, _direction2)

        camera_view(_i + 1)

        for i in range(3):
            _direction2 = (i+3) % 4
            view_check(_r, _c, i, 1)
            view_check(_r, _c, _direction2)
            camera_view(_i + 1)

        _direction = -1
        for i in range(3):
            _direction2 = (_direction+i) % 4
            view_check(_r, _c, _direction2, 1)


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
CCTVs = []
drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]    # 상우하좌(시계방향)
blind_area_cnt = 0
min_blind_cnt = N*M
for r in range(N):
    for c in range(M):
        if 0 < office[r][c] < 5:
            CCTVs.append((r, c, office[r][c]))

        elif office[r][c] == 5:
            for direction in range(4):
                view_check(r, c, direction)

# 사각지대 수 카운트
blind_area_cnt = 0  # 위의 cctv5를 확인하면서 값이 변해서 다시 초기화
for r in range(N):
    for c in range(M):
        if office[r][c] == 0:
            blind_area_cnt += 1

camera_view()

print(min_blind_cnt)
