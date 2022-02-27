# 주사위 게임
import sys
input = sys.stdin.readline

N = int(input())
result = []
for _ in range(N):
    a, b, c = map(int, input().split())

    if a == b == c:
        result.append(10000 + 1000*a)

    elif a == b or a == c:
        result.append(1000+100*a)

    elif b == c:
        result.append(1000+100*b)

    else:
        result.append(100*max(a, b, c))

print(max(result))
