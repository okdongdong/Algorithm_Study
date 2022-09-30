def ccw(a, b, c):
    result = (b[0] - a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

    if result > 0:
        return 1

    if result < 0:
        return -1

    return 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A, B, C, D = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

print(int(ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(C, D, A)*ccw(C, D, B) < 0))
