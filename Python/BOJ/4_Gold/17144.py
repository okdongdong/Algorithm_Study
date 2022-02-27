# 미세먼지 안녕!

def dust_circulation(sr, is_down=True):
    global dust
    dir_idx = 0 if is_down else 2
    _r = sr + drc[dir_idx][0]
    _c = 0
    while (_r, _c) != (sr, 1):
        _dr, _dc = drc[dir_idx]
        nr = _r+_dr
        nc = _c+_dc

        if (nr >= R or nr < 0) or (nc >= C or nc < 0) or (is_down and nr < sr) or (not is_down and nr > sr):
            dir_idx += 1 if is_down else -1
            dir_idx %= 4
            continue

        room[_r][_c] = room[nr][nc]
        dust[(_r, _c)] = room[nr][nc]

        _r, _c = nr, nc

    if room[sr][1]:
        room[sr][1] = 0
        del dust[(sr, 1)]


def dust_spread():  # 먼지확산
    global dust
    check_list = set()
    xr = air_cleaner[0]
    for (_r, _c), _val in dust.items():   # 좌표, 먼지양
        spread_val = _val//5
        check_list.add((_r, _c))
        for _dr, _dc in drc:    # 확산
            nr = _r+_dr
            nc = _c+_dc
            if (nr == xr or nr == xr-1) and nc == 0:
                continue

            if 0 <= nr < R and 0 <= nc < C and _val > 4:

                room[nr][nc] += spread_val
                room[_r][_c] -= spread_val
                check_list.add((nr, nc))
    temp = {}
    for _r, _c in check_list:
        temp[(_r, _c)] = room[_r][_c]

    dust = temp

    dust_circulation(air_cleaner[0], True)      # 아래쪽
    dust_circulation(air_cleaner[0]-1, False)   # 위쪽


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]    # 하우상좌(반시계)
dust = {}

# 먼지, 공청기 위치 찾기
for r in range(R):
    for c in range(C):
        if room[r][c] > 0:
            dust[(r, c)] = room[r][c]     # 확산시 오류방지위해 먼지양까지 함께 저장
        elif room[r][c] < 0:
            air_cleaner = (r, c)    # 아래쪽 좌표 저장

# 먼지 확산
for _ in range(T):
    dust_spread()

# 먼지양 계산
result = sum(map(sum, room)) + 2    # 공청기 값 추가

print(result)
