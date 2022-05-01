# Z

N, r, c = map(int, input().split())
num = 2**N
result = 0

while num > 1:
    num //= 2

    if r >= num:
        result += num**2 * 2
        r -= num

    if c >= num:
        result += num**2
        c -= num

print(result)
