N = int(input())
tree = list(map(int, input().split()))
del_node = int(input())

childs = [[] for _ in range(N + 1)]
root_node = 0

for c, p in enumerate(tree):
    if p == -1:
        root_node = c
        continue

    if c == del_node:
        continue

    childs[p].append(c)

childs[del_node] = []
stack = [root_node]
cnt = 0

while stack:
    node = stack.pop()
    if node == del_node:
        continue

    if not childs[node]:
        cnt += 1

    for child in childs[node]:
        stack.append(child)

print(cnt)
