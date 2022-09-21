N, M, V = map(int, input().split())
edges = [set() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

edges = list(map(sorted, edges))

result = []
visited = [False]*(N+1)


def dfs(node):
    visited[node] = True
    result.append(node)
    for next_node in edges[node]:
        if visited[next_node]:
            continue
        dfs(next_node)

    return result


def bfs(start_node):
    que = [start_node]
    visited = [False]*(N+1)
    visited[start_node] = True
    result = []

    while que:
        temp = []
        for node in que:
            result.append(node)

            for next_node in edges[node]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                temp.append(next_node)

        que = temp

    return result


print(*dfs(V))
print(*bfs(V))
