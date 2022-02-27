# 정사각형
import sys
input = sys.stdin.readline

def cal_length(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5


T = int(input())
result = []
for tc in range(T):
    points = [list(map(int, input().split())) for _ in range(4)]
    length_list = []

    for i in range(3):
        for j in range(i+1, 4):
            length_list.append(cal_length(*points[i], *points[j]))

    r1, r2, r3, r4, d1, d2 = sorted(length_list)

    if r1 == r2 == r3 == r4 and d1 == d2:
        result.append("1")
    else:
        result.append("0")
        
print("\n".join(result))