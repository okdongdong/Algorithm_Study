import sys

input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

broken_road = set()
for _ in range(K):
    a, b, c, d = map(int, input().split())
    if (a, b) > (c, d):
        a, b, c, d = c, d, a, b

    broken_road.add((a, b, c, d))

arr = [[0] * (M + 2) for _ in range(N + 2)]
arr[0][0] = 1

for r in range(N + 1):
    for c in range(M + 1):
        arr[r][c + 1] += arr[r][c] * (not (r, c, r, c + 1) in broken_road)
        arr[r + 1][c] += arr[r][c] * (not (r, c, r + 1, c) in broken_road)

print(arr[N][M])
