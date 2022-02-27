# 바이러스
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
tree = [[] for _ in range(N+1)]
check = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

stack = [1]
while stack:
    next_node = stack.pop()
    check[next_node] = 1
    for node in tree[next_node]:
        if not check[node]:
            stack.append(node)

print(sum(check)-1)
