# 온풍기 안녕!

# 바람! => 온도! => 최외곽 온도 1도 감소
# 초코!
# 조사하는 모든 칸의 온도가 K 이상일 때까지 반복
# 좌상한 (1, 1)
# 칸과 칸사이 벽
import sys
import copy
input = sys.stdin.readline


def wind(_r, _c, _direction):
    dr, dc = drc[_direction]
    side_drc = (drc[(_direction-1) % 4], drc[(_direction+1) % 4])
    # 온풍기 바로앞은 무조건 존재하므로 그냥 더해줌
    _r += dr
    _c += dc
    heat_area[_r][_c] += 5
    stack = set([(_r, _c)])
    for heat in range(4, 0, -1):
        temp = set()
        temp = copy.deepcopy(stack)

        # 사이드 방향 이동 체크
        for r, c in stack:
            for _dr, _dc in side_drc:
                nr = r+_dr
                nc = c+_dc
                if 0 <= nr < R and 0 <= nc < C and (not wall_dict.get((nr, nc)) or (_dr, _dc) not in wall_dict[(nr, nc)]):
                    temp.add((nr, nc))

        # 전방 이동 체크
        next_temp = set()
        for r, c in temp:
            nr = r+dr
            nc = c+dc
            if 0 <= nr < R and 0 <= nc < C and (not wall_dict.get((nr, nc)) or (dr, dc) not in wall_dict[(nr, nc)]):
                next_temp.add((nr, nc))
                heat_area[nr][nc] += heat
        stack = next_temp


def temperature():
    for r in range(R):
        for c in range(C):
            for dr, dc in drc:
                nr = r+dr
                nc = c+dc
                if 0 <= nr < R and 0 <= nc < C and (not wall_dict.get((nr, nc)) or (dr, dc) not in wall_dict[(nr, nc)]):
                    if heat_area[r][c] > heat_area[nr][nc]:
                        temp_heat_area[nr][nc] += (heat_area[r][c] - heat_area[nr][nc])//4
                        temp_heat_area[r][c] -= (heat_area[r][c] - heat_area[nr][nc])//4
    for r in range(R):
        for c in range(C):
            heat_area[r][c] += temp_heat_area[r][c]
            temp_heat_area[r][c] = 0


R, C, K = map(int, input().split())
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 동남서북(시계방향)
air_heaters_drc = {1: 0, 2: 2, 3: 3, 4: 1}
heat_area = [[0]*C for _ in range(R)]
temp_heat_area = [[0]*C for _ in range(R)]
my_room = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
walls = [list(map(int, input().split())) for _ in range(W)]
wall_dict = dict()
choco = 0

air_heaters = []
check_areas = []
# 온풍기, 온도 조사 위치 체크
for r in range(R):
    for c in range(C):
        if my_room[r][c] == 5:
            check_areas.append((r, c))
        elif my_room[r][c]:
            air_heaters.append((r, c, air_heaters_drc[my_room[r][c]]))

# 벽 위치 체크
for r, c, t in walls:
    if t:
        try:
            wall_dict[(r-1, c-1)].add((0, -1))
        except:
            wall_dict[(r-1, c-1)] = set([(0, -1)])
        try:
            wall_dict[(r-1, c)].add((0, 1))
        except:
            wall_dict[(r-1, c)] = set([(0, 1)])
    else:
        try:
            wall_dict[(r-2, c-1)].add((-1, 0))
        except:
            wall_dict[(r-2, c-1)] = set([(-1, 0)])
        try:
            wall_dict[(r-1, c-1)].add((1, 0))
        except:
            wall_dict[(r-1, c-1)] = set([(1, 0)])

# 초코!
while choco < 101:
    # 바람!
    for hr, hc, d in air_heaters:
        wind(hr, hc, d)

    # 온도!
    temperature()

    # 테두리 온도 1감소
    for r in range(1, R-1):
        if heat_area[r][0]:
            heat_area[r][0] -= 1
        if heat_area[r][-1]:
            heat_area[r][-1] -= 1

    for c in range(C):
        if heat_area[0][c]:
            heat_area[0][c] -= 1
        if heat_area[-1][c]:
            heat_area[-1][c] -= 1

    # 초코!
    choco += 1

    # 모든칸의 온도가 K이상이면 while문 탈출
    for r, c in check_areas:
        if heat_area[r][c] < K:
            break
    else:
        break

print(choco)
