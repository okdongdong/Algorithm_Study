# 돌 그룹
import sys
sys.setrecursionlimit(10**6)


def cal(a, b, c):
    global result
    if (a, b, c) in pre_cases:
        return

    pre_cases.add((a, b, c))

    if result:
        return

    if a == b:
        if b == c:
            result = 1
            return
        elif b*2 == c:
            return

        cal(*sorted([a, 2*b, c-b]))
        return

    elif a*2 == b and b == c:
        return

    cal(*sorted([a, 2*b, c-b]))
    cal(*sorted([b, 2*a, c-a]))


A, B, C = map(int, input().split())
result = 0
pre_cases = set()

if (A+B+C) % 3 == 0:
    cal(*sorted([A, B, C]))

print(result)
