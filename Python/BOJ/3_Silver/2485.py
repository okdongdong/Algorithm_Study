import sys

input = sys.stdin.readline


def euclidean(a, b):
    if a < b:
        a, b = b, a

    a, b = b, a % b

    if b == 0:
        return a

    return euclidean(a, b)


N = int(input())
trees = [int(input()) for _ in range(N)]
trees.sort()
distances = []

for i in range(N - 1):
    distances.append(trees[i + 1] - trees[i])

gcd = distances[0]
for i in range(1, N - 1):
    gcd = euclidean(gcd, distances[i])

cnt = 0
for distance in distances:
    cnt += distance // gcd - 1

print(cnt)
