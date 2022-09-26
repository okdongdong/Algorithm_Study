from math import ceil

a, b, c = map(int, input().split())

print(max(0, ceil((b-a)/c)))
