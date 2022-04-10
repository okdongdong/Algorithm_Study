# 평행사변형

x1, y1, x2, y2, x3, y3 = map(int, input().split())

if (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3) == 0:
    print(-1)

else:
    s1 = ((x1-x2)**2 + (y1-y2)**2)**.5
    s2 = ((x1-x3)**2 + (y1-y3)**2)**.5
    s3 = ((x3-x2)**2 + (y3-y2)**2)**.5

    min_s, mid_s, max_s = sorted([s1, s2, s3])

    print(2*(max_s - min_s))
