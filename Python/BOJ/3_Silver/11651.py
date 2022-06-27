import sys

input = sys.stdin.readline

N = int(input())
positions = [list(map(int, input().split())) for _ in range(N)]
positions.sort(key=lambda x: (x[1], x[0]))

for position in positions:
    print(*position)
