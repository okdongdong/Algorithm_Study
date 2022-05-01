N, B = input().split()
B = int(B)
result = 0
for i in range(len(N)):
    n = N[i]
    if n.isnumeric():
        n = int(n)
    else:
        n = ord(n)-55

    result += n * (B ** (len(N)-i-1))

print(result)
