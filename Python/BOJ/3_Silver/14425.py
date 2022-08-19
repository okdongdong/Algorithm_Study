import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = {input().rstrip() for _ in range(N)}
cnt = 0

for _ in range(M):
    if input().rstrip() in S:
        cnt += 1

print(cnt)
