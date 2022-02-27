# 플로이드

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
cost_arr = [[987654321]*n for _ in range(n)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    start -= 1
    end -= 1
    cost_arr[start][end] = min(cost_arr[start][end], cost)

for now_city in range(n):
    for start in range(n):
        if now_city == start:
            continue

        for end in range(n):
            if now_city == end:
                continue

            if start == end:  # 시작도시와 도착도시가 같은 경우는 없음
                cost_arr[start][end] = 0
                continue

            cost_arr[start][end] = min(cost_arr[start][end], cost_arr[start][now_city]+cost_arr[now_city][end])

for start in range(n):
    for end in range(n):
        if cost_arr[start][end] == 987654321:
            cost_arr[start][end] = 0

for result_cost in cost_arr:
    print(*result_cost)
