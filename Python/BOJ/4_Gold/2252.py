# 줄 세우기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
a_to_b = [[] for _ in range(N+1)]
in_node_cnt = [0]*(N+1)

for a, b in edges:
    in_node_cnt[b] += 1
    a_to_b[a].append(b)

start_node = []
for idx, cnt in enumerate(in_node_cnt):
    if idx == 0:
        continue
    if cnt == 0:
        start_node.append(idx)
idx = 0
while idx < len(start_node):
    a = start_node[idx]
    for node in a_to_b[a]:
        in_node_cnt[node] -= 1
        if in_node_cnt[node] == 0:
            start_node.append(node)
    idx += 1

print(' '.join(map(str, start_node)))