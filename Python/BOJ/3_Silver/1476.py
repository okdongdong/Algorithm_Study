# 날짜계산
E, S, M = map(int, input().split())
while not (E == S == M):
    if min(E, S, M) == E:
        E += 15
    elif min(E, S, M) == S:
        S += 28
    else:
        M += 19
print(E)
