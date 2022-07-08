# 접두사

import sys

input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
words.sort(key=len)
result = set()

for i in range(N-1):
    w1 = words[i]

    for j in range(i+1, N):
        w2 = words[j]

        if w2.startswith(w1):
            break

    else:
        result.add(w1)

print(len(result))
