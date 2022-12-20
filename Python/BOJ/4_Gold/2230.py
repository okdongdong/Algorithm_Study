import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()

s, e = 0, 1
min_diff = float("inf")

while s < N and e < N:
    if s >= e:
        e += 1
        continue

    diff = A[e] - A[s]

    if M <= diff:
        min_diff = min(min_diff, diff)

    if diff >= min_diff:
        s += 1
    else:
        e += 1

print(min_diff)
