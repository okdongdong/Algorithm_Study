from itertools import combinations as comb

N, M = map(int, input().split())
for nums in sorted(comb(range(1, N + 1), M)):
    print(*nums)
