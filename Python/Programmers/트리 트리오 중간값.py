def solution(n, edges):
    nodes = [[] for _ in range(n+1)]
    for i in range(n-1):
        s, e = edges[i]
        nodes[s].append(e)
        nodes[e].append(s)

    # 리프노드 중 아무거나 하나를 탐색(1)
    for node, node_list in enumerate(nodes):
        if len(node_list) == 1:
            cnt_list = bfs(node, n, nodes)
            break

    # 찾은 리프노드(1)에서 가장 멀리 떨어진 리프노드(2) 탐색
    node = cnt_list.index(max(cnt_list))
    cnt_list = bfs(node, n, nodes)
    
    # (1)에서 탐색시 (2)가 유일할 수 있지만 (2)에서 탐색시 (1)과 같은 거리의 리프노드가 존재할 수 있으므로 (2)에서 재탐색
    node = cnt_list.index(max(cnt_list))

    cnt_list.sort(reverse=True)
    answer = cnt_list[1]

    cnt_list = bfs(node, n, nodes)
    cnt_list.sort(reverse=True)
    answer = max(answer, cnt_list[1])

    return answer


def bfs(s_node, n, nodes):
    visited = [False]*(n+1)

    que = [s_node]
    cnt_list = [0]*(n+1)
    cnt = 0
    while que:
        temp = []
        for node in que:
            if visited[node]:
                continue

            cnt_list[node] = cnt
            visited[node] = True
            for n_node in nodes[node]:
                temp.append(n_node)

        que = list(set(temp))
        cnt += 1

    return cnt_list


print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(5, [[1, 5], [2, 5], [3, 5], [4, 5]]))
