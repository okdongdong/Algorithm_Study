# 스타트 택시
import sys

input = sys.stdin.readline


def find_passenger(_r, _c):
    flag = False
    temp_passengers = []
    _fuel_usage = 0
    if taxi_map[_r][_c] == 2:
        taxi_map[_r][_c] = 0
        return _r, _c, _fuel_usage

    stack = [(_r, _c)]
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    while stack:
        temp = []
        _fuel_usage += 1
        for _r, _c in stack:
            for dr, dc in drc:
                if 0 <= _r + dr < N + 1 and 0 <= _c + dc < N + 1 and not visited[_r + dr][_c + dc]:
                    visited[_r + dr][_c + dc] = True
                    if taxi_map[_r + dr][_c + dc] == 2:
                        temp_passengers.append((_r + dr, _c + dc))
                        flag = True
                    elif taxi_map[_r + dr][_c + dc] != 1:
                        temp.append((_r + dr, _c + dc))
        if flag:
            temp_passengers.sort()
            taxi_map[temp_passengers[0][0]][temp_passengers[0][1]] = 0
            return temp_passengers[0][0], temp_passengers[0][1], _fuel_usage
        stack = temp
    return None


def passenger_to_goal(_r, _c, _g_r, _g_c):
    _fuel_usage = 0
    stack = [(_r, _c)]
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    while stack:
        temp = []
        _fuel_usage += 1
        for _r, _c in stack:
            for dr, dc in drc:
                if 0 <= _r + dr < N + 1 and 0 <= _c + dc < N + 1 and not visited[_r + dr][_c + dc]:
                    visited[_r + dr][_c + dc] = True
                    if _r + dr == _g_r and _c + dc == _g_c:
                        return _fuel_usage
                    elif taxi_map[_r + dr][_c + dc] != 1:
                        temp.append((_r + dr, _c + dc))
        stack = temp
    return None


N, M, fuel = map(int, input().split())
taxi_map = [[1] * (N + 1)] + [[1] + list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
passengers = [list(map(int, input().split())) for _ in range(M)]
goals = {}

drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 승객 우선순위에 따라 drc 배정

# 손님, 목적지 표시
for s_r, s_c, e_r, e_c in passengers:
    taxi_map[s_r][s_c] = 2  # 손님
    goals[(s_r, s_c)] = (e_r, e_c)  # 목적지

# BFS
cnt = 0
while cnt < M:
    try:
        r, c, fuel_usage = find_passenger(r, c)
        fuel -= fuel_usage
        g_r, g_c = goals[(r, c)]

        fuel_usage = passenger_to_goal(r, c, g_r, g_c)
        fuel -= fuel_usage

        if fuel < 0:
            fuel = -1
            break
        else:
            fuel += fuel_usage * 2
    except:
        fuel = -1
        break

    r, c = g_r, g_c
    cnt += 1

print(fuel)
