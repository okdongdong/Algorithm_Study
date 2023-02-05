from itertools import permutations

N, M = map(int, input().split())
for n in permutations(range(1, N + 1), M):
    print(*n)
