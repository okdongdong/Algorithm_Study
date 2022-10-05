x, k = map(int, input().split())
x = 1000*x
result = 0

if x >= 1750*k:
    result = 1750*k
if x >= 3500*k:
    result = 3500*k
if x >= 7000*k:
    result = 7000*k

print(result)
