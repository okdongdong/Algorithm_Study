# 최단경로
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())
next_node_list = [(0, S)]
nodes = [dict() for _ in range(V+1)]
distanse = [987654]*(V+1)
distanse[S] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    if nodes[u].get(v):
        nodes[u][v] = min(w, nodes[u][v])
    else:
        nodes[u][v] = w

while next_node_list:
    w, now_node = heapq.heappop(next_node_list)
    for next_node, w in nodes[now_node].items():
        if distanse[next_node] > distanse[now_node]+w:
            distanse[next_node] = distanse[now_node]+w
            heapq.heappush(
                next_node_list, (distanse[next_node], next_node))

result = list(map(lambda x: 'INF' if x ==
              987654 else str(x), distanse[1:]))
print('\n'.join(result))
