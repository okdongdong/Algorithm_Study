# 최소 스패닝 트리
V, E = map(int, input().split())
edges = {}
edges2 = [[] for _ in range(V)]
for _ in range(E):
    A, B, C = map(int, input().split())
    if A < B:
        edges[(A-1, B-1)] = C
    else:
        edges[(B-1, A-1)] = C
    
    edges2[A-1].append(B-1)
    edges2[B-1].append(A-1)

visited = [False]*V
min_val = [1000001]*V

min_val[0] = 0
min_idx = 0

for _ in range(V):
    next_min_idx = 0
    now_min_val = 10000001
    for i in edges2[min_idx]:
        if visited[i]:
            continue
        if now_min_val > min_val[i]:
            next_min_idx = i
            now_min_val = min_val[i]

    visited[next_min_idx] = True
     
    for i in range(V):
        if visited[i] or i == next_min_idx:
             continue
        if min_val[i] > edges[(min(next_min_idx, i), max(next_min_idx, i))]:
            min_val[i] = edges[(min(next_min_idx, i), max(next_min_idx, i))]
    
    min_idx = next_min_idx
print(sum(min_val))