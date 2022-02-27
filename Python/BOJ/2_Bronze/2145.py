# 숫자 놀이

import sys
input = sys.stdin.readline
result = []
while True:
    N = int(input())
    if not N:
        break
    while True:
        temp = 0
        while N:
            N, M = divmod(N, 10)
            temp += M

        N = temp
        if N < 10:
            break
    result.append(str(N))

print('\n'.join(result))
