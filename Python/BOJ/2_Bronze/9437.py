# 사라진 페이지 찾기

import sys

input = sys.stdin.readline

while True:
    try:
        N, P = map(int, input().split())

    except:
        break

    p = ((P+1)//2)*2 - 1

    pages = sorted([p, p+1, N-p, N-p+1])
    pages.remove(P)

    print(*pages)
