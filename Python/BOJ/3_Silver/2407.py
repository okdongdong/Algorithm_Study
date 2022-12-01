n, m = map(int, input().split())
m = min(m, n - m)
a, b = 1, 1
while m:
    a *= n
    b *= m
    n -= 1
    m -= 1

print(a // b)
