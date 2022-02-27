T = int(input())

for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    stars = []
    cnt = 0

    for j in range(n):
        stars.append(list(map(int, input().split())))  # 행성계의 좌표

    for cx, cy, r in stars:  # 행성계 중심과 현재&도착 위치의 거리 <> 행성계 반지름 비교해서 판단
        r1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        r2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5
        if (r1 < r < r2) or (r2 < r < r1):
            cnt += 1

    print(cnt)
