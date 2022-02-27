def bridge(a, b):

    n, m = 1, 1

    if a == b:
        return 1

    else:
        for i in range(1, a + 1):
            m *= i

        for i in range(b, b-a, -1):
            n *= i

        return int(n/m)

N = int(input())

lst = []

for i in range(N):
    a, b = map(int, input().split())
    lst.append(str(bridge(a, b)))

print('\n'.join(lst))
