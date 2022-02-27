# 드래곤 커브
import sys
input = sys.stdin.readline


def dragon_curve(_x, _y, _d_list, _g):
    global dragon_curve_points

    dragon_curve_points.add((_x, _y))

    if _g > g:
        return

    _next_d_list = _d_list[:]

    for i in range(len(_d_list)-1, -1, -1):
        _d = _d_list[i]
        dx, dy = dxy[_d]
        _x += dx
        _y += dy
        dragon_curve_points.add((_x, _y))
        _next_d_list.append((_d+1) % 4)  # 결국 반시계 방향으로 돌려서 이동하는 거랑 같음

    dragon_curve(_x, _y, _next_d_list, _g + 1)


N = int(input())
dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 우상좌하
dragon_curve_points = set()
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve_points.add((x, y))
    dx, dy = dxy[d]

    dragon_curve(x+dx, y+dy, [(d+1) % 4], 1)

cnt = 0
for x, y in dragon_curve_points:
    if (x+1, y) in dragon_curve_points and (x, y+1) in dragon_curve_points and (x+1, y+1) in dragon_curve_points:
        cnt += 1

print(cnt)
