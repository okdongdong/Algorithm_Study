def distance(x1, y1, r1, x2, y2, r2):
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if r == 0:
        if r1 == r2:
            return -1
        else:
            return 0
    else:
        if r == abs(r1 - r2) or r == r1 + r2:
            return 1
        elif abs(r1 - r2) < r < r1 + r2:
            return 2
        else:
            return 0


n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(distance(x1, y1, r1, x2, y2, r2))
