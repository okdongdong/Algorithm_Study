from collections import deque


def solution(n, path, order):
    edges = [[] for _ in range(n)]
    prev_nodes = [set() for _ in range(n)]
    next_nodes = [set() for _ in range(n)]

    for a, b in path:
        edges[a].append(b)
        edges[b].append(a)

    for a, b in order:
        prev_nodes[b].add(a)
        next_nodes[a].add(b)

    # 유일한 입구는 0번노드와 연결
    visited = [False] * n
    visited[0] = True
    visit_cnt = 0
    que = deque([0])

    while que:
        now_node = que.popleft()
        visit_cnt += 1
        for next_node in next_nodes[now_node]:
            prev_nodes[next_node].discard(now_node)

            # 선행노드를 모두 방문한 노드를 이미 방문한경우 que에 추가
            if not prev_nodes[next_node] and visited[next_node]:
                que.append(next_node)

        next_nodes[now_node].clear()

        for next_node in edges[now_node]:
            if visited[next_node]:
                continue

            visited[next_node] = True

            # 선행노드가 남아있다면 그냥 넘김, 방문체크 후 위에서 다시 추가
            if prev_nodes[next_node]:
                continue

            que.append(next_node)

    return visit_cnt == n


print(
    solution(
        9,
        [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]],
        [[8, 5], [6, 7], [4, 1]],
    )
)
print(
    solution(
        9,
        [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]],
        [[4, 1], [5, 2]],
    )
)
print(
    solution(
        9,
        [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]],
        [[4, 1], [8, 7], [6, 5]],
    )
)
