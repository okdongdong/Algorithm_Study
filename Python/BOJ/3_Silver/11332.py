# 시간초과
C = int(input())
result = []
for _ in range(C):
    S, N, T, L = input().split()
    N, T, L = map(int, (N, T, L))
    time_limit = 10**8 * L
    time_over = True
    if S == 'O(N)':
        if N * T <= time_limit:
            time_over = False

    elif S == 'O(N^2)':
        if N**2 * T <= time_limit:
            time_over = False

    elif S == 'O(N^3)':
        if N**3 * T <= time_limit:
            time_over = False

    elif S == 'O(2^N)':
        temp = T
        for _ in range(N):
            temp *= 2
            if temp >= time_limit:
                break
        else:
            time_over = False

    else:
        temp = T
        for i in range(N, 0, -1):
            temp *= i
            if temp >= time_limit:
                break
        else:
            time_over = False

    result.append('TLE!' if time_over else 'May Pass.')

print('\n'.join(result))
