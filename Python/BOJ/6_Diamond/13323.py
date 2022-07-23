# BOJ 수열 1

from heapq import heappop, heappush

N = int(input())
A_sequence = list(map(int, input().split()))
result = 0
que = []

for i in range(N):
    num = i - A_sequence[i]
    heappush(que, num)

    if que[0] < num:
        result += num - heappop(que)
        heappush(que, num)

print(result)
