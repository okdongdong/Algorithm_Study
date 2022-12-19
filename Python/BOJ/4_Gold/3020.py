import sys

input = sys.stdin.readline

N, H = map(int, input().split())
rock = [0] * (H + 1)
cave = [0] * (H + 1)

for i in range(N):
    h = int(input())
    if i % 2:
        rock[H - h] += 1
        rock[-1] -= 1
    else:
        rock[0] += 1
        rock[h] -= 1

for h in range(H + 1):
    cave[h] = cave[h - 1] + rock[h]

cave.pop()
min_val = min(cave)
print(min_val, cave.count(min_val))
