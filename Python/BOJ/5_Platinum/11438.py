# LCA 2
import sys

input = sys.stdin.readline

N = int(input())
max_level = 17  # 2**17 > 100,000
tree = [[0]*max_level for _ in range(N+1)]
node_level = [0] * (N+1)
nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

# 부모노드 설정
visited = [False]*(N+1)
stack = [1]

while stack:
    parent = stack.pop()
    visited[parent] = True

    for node in nodes[parent]:
        if visited[node]:
            continue
        node_level[node] = node_level[parent] + 1
        tree[node][0] = parent
        stack.append(node)

for level_2 in range(1, max_level):
    for node in range(1, N+1):
        ancestor = tree[node][level_2-1]
        # next ancestor
        tree[node][level_2] = tree[ancestor][level_2-1]


# 조상 찾기
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if node_level[a] > node_level[b]:
        a, b = b, a

    for level in range(max_level-1, -1, -1):
        if node_level[b] - node_level[a] >= 1 << level:
            b = tree[b][level]

    if a == b:
        print(a)
        continue

    for level in range(max_level-1, -1, -1):
        # 2**level만큼 점프뛰면서 조상을 탐색

        if tree[a][level] == tree[b][level]:
            # 2**level 번째 위의 조상이 같다면 올라가지말고 좀 더 적게 점프 뛰어야함
            continue

        # 2**level번째 조상이 다르다면 올라감
        a = tree[a][level]
        b = tree[b][level]

    print(tree[a][0])
