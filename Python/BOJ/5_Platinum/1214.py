D, P, Q = map(int, input().split())

Q, P = sorted((P, Q))

N = D//P + 1
min_D = P*N

for n in range(N-1, -1, -1):
    d, m = divmod(D - P*n, Q)
    if m == 0:
        min_D = D
        break

    value = P*n + Q*(d+1)
    if value == min_D:
        break

    min_D = min(min_D, value)

print(min_D)
