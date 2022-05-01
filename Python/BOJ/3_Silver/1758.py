import sys
input = sys.stdin.readline

N = int(input())
result = 0
tip = [int(input()) for _ in range(N)]
tip.sort(reverse=True)
for i in range(N):
    if tip[i]-i < 0:
        break

    result += tip[i]-i

print(result)
