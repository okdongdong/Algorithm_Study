N, K = map(int, input().split())

result = 0
while bin(N).count('1') > K:
    for i in range(len(bin(N))):
        if (1 << i) & N:
            N += 1 << i
            result += 1 << i
            break

print(result)
