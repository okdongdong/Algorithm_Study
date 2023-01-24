import sys

input = sys.stdin.readline


def union(a, b):
    head_a = find(a)
    head_b = find(b)
    head[head_b] = head_a


def find(a):
    if head[a] != a:
        head[a] = find(head[a])
    return head[a]


N, M = map(int, input().split())
head = list(range(N + 1))
for _ in range(M):
    c, a, b = map(int, input().split())
    c or union(a, b)
    c and print(["NO", "YES"][find(a) == find(b)])
