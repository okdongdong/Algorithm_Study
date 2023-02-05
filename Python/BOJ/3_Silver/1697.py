from collections import deque

N, K = map(int, input().split())
L = 100000
visited = [0] * (L + 1)
visited[N] = 1


def set_val(a, n):
    visited[a] = visited[n] + 1


que = deque([N])
while que:
    n = que.popleft()
    if n == K:
        break
    a, b, c = n - 1, n + 1, n * 2
    a < 0 or visited[a] or set_val(a, n) or que.append(a)
    b > L or visited[b] or set_val(b, n) or que.append(b)
    c > L or visited[c] or set_val(c, n) or que.append(c)

print(visited[K] - 1)
