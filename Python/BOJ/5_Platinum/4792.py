# 레드 블루 스패닝 트리

result = []
while 1:
    n, m, k = map(int, input().split())  # n: 정점의 개수, m: 간선의 개수, k: 파란색 간선의 개수
    if n == 0:
        break
    edges = [[] for _ in range(n+1)]
    blue_cnt = 0
    red_cnt = 0
    for _ in range(m):
        c, f, l = input().split()
        f = int(f)
        l = int(l)
        if c == 'B':
            edges[f].append((l, 1))
            edges[l].append((f, 1))
            blue_cnt += 1
        else:
            edges[f].append((l, 0))
            edges[l].append((f, 0))
            red_cnt += 1

    if blue_cnt < k or red_cnt + k < n-1 or m < n-1 or m < k:
        # 파란 간선의 개수가 요구사항보다 적을 때
        # 빨간 간선의 개수와 파란 간선 요구사항의 합이 스패닝 트리의 간선 수보다 적을 때
        # 스패닝 트리가 될 만큼의 간선이 없을 때
        # 간선의 수가 요구사항보다 적을 때
        result.append('0')
        continue

    visited = [False]*(n+1)
    edges_val_max = [0]*(n+1)
    edges_val_min = [1]*(n+1)
    stack = [1]
    while stack:
        idx = stack.pop()
        visited[idx] = True
        for i, val in edges[idx]:
            # 파란 간선을 최대로 하여 스패닝 트리 구성
            edges_val_max[i] = max(edges_val_max[i], val)
            # 파란 간선을 최소로 하여 스패닝 트리 구성
            edges_val_min[i] = min(edges_val_min[i], val)
            if visited[i]:
                continue
            stack.append(i)

    edges_val_max[0], edges_val_max[1] = 0, 0
    edges_val_min[0], edges_val_min[1] = 0, 0

    max_k = sum(edges_val_max)
    min_k = sum(edges_val_min)

    if min_k <= k <= max_k:
        result.append('1')
    else:
        result.append('0')

print('\n'.join(result))
