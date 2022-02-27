# Fly me to the Alpha Centauri

N = int(input())
result = []
for _ in range(N):
    a, b = map(int, input().split())
    dis = b-a-1
    n = int(dis**0.5)
    if n**2 <= dis < n*(n+1):
        result.append(2*n)
    else:
        result.append(2*n+1)

print(*result, sep='\n')
