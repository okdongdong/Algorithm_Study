def gcd(a, b):
    b, a = sorted((a, b))

    while b:
        a, b = b, a % b

    return a


N = int(input())
rings = list(map(int, input().split()))

for i in range(1, N):
    A, B = rings[0], rings[i]
    C = gcd(A, B)

    print(f'{A//C}/{B//C}')
