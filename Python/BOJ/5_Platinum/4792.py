# 레드 블루 스패닝 트리
from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def check(is_max_heap=False):
    visited = [False] * (n+1)
    que = [(0, 1)]
    cnt = 0
    blue_cnt = 0
    while que and cnt < n:
        val1, f_node = heappop(que)
        if visited[f_node]:
            continue

        cnt += 1
        if val1 != 0:
            blue_cnt += 1

        visited[f_node] = True
        for val2, l_node in edges[f_node]:
            heappush(que, (val2*(-1)**is_max_heap, l_node))

    return blue_cnt


while True:
    n, m, k = map(int, input().split())
    if n == 0:
        break

    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        c, f, l = input().split()
        f = int(f)
        l = int(l)
        val = int(c == 'B')
        edges[f].append((val, l))
        edges[l].append((val, f))

    max_k = check(True)
    min_k = check(False)

    print(int(min_k <= k <= max_k))
