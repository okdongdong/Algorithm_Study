N, M = int(input()), int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
schedule = list(map(int, input().split()))
head = list(range(N))


def find(n):
    if head[n] != n:
        head[n] = find(head[n])

    return head[n]


def union(a, b):
    head_a = find(a)
    head_b = find(b)
    head[head_b] = head[head_a]


for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i][j]:
            union(i, j)

for i in range(M - 1):
    a, b = schedule[i] - 1, schedule[i + 1] - 1
    if find(a) != find(b):
        print("NO")
        break

else:
    print("YES")
