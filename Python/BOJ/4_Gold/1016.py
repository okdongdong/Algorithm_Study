import math

a, b = map(int, input().split())

tb = [True] * (b - a + 1)
squared_nums = []

for i in range(2, int(b**0.5)+1):
    squared_nums.append(i**2)

for i in squared_nums:
    j = math.ceil(a/i)
    while i*j <= b:
        tb[i*j-a] = False
        j += 1

print(sum(tb))
