# 보물찾기

import sys
input = sys.stdin.readline

N = int(input())
tree = [set() for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)

node_rank_list = [0]*(N+1)
next_node_list = set()
rank = 0
for i in range(1, N+1):
    if len(tree[i]) == 1:
        next_node_list.add(i)   # 리프노드 추가

while next_node_list:
    temp = set()
    for node in next_node_list:
        temp_next_node = set()
        temp_next_node.update(tree[node])
        for next_node in temp_next_node:
            if node_rank_list[next_node] == node_rank_list[node]:
                if len(tree[node]) > 1:
                    node_rank_list[node] += 1
                else:
                    node_rank_list[next_node] += 1
            else:
                node_rank_list[next_node] = max(node_rank_list[next_node], node_rank_list[node]+1)  # 차수 입력

            tree[node].discard(next_node)   # 간선 끊기
            tree[next_node].discard(node)
            temp.add(next_node)
    next_node_list = temp

print(max(node_rank_list))





