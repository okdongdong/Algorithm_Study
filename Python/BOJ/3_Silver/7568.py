import sys
input = sys.stdin.readline

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
result = []
for w1, h1 in people:
    cnt = 1
    for w2, h2 in people:
        if w1 < w2 and h1 < h2:
            cnt += 1
    result.append(cnt)

print(*result)
