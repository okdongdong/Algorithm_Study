def solution(arrows):
    # 대각선이 크로스 되는 경우 고려해주기 위해 대각방향은 절반씩 두번이동
    directions = [[0, 2], [1, 1], [2, 0], [1, -1], [0, -2], [-1, -1], [-2, 0], [-1, 1]]
    node_visited = set([(0, 0)])
    edge_visited = set()
    r, c = 0, 0
    answer = 0

    def move(arrow):
        nonlocal answer
        dr, dc = directions[arrow]
        nr, nc = r + dr, c + dc

        # 이미 방문한 간선이면 통과
        if (r, c, nr, nc) in edge_visited:
            return nr, nc

        # 방문한적 없는 간선을 통해서 방문했던 노드 방문 => 도형완성
        if (nr, nc) in node_visited:
            answer += 1

        # 노드 방문체크
        node_visited.add((nr, nc))

        # 양방향 간선 방문체크
        edge_visited.add((r, c, nr, nc))
        edge_visited.add((nr, nc, r, c))

        return nr, nc

    for arrow in arrows:
        r, c = move(arrow)

        if arrow % 2:
            r, c = move(arrow)

    return answer


def solution2(arrows):
    # 대각선이 크로스 되는 경우 고려해주기 위해 대각방향은 절반씩 두번이동
    directions = [[0, 2], [1, 1], [2, 0], [1, -1], [0, -2], [-1, -1], [-2, 0], [-1, 1]]
    node_visited = set([(0, 0)])
    edge_visited = set()
    r, c = 0, 0

    for arrow in arrows:
        dr, dc = directions[arrow]
        for _ in range(1 + arrow % 2):
            nr, nc = r + dr, c + dc

            node_visited.add((nr, nc))
            edge_visited.add((r, c, nr, nc))
            edge_visited.add((nr, nc, r, c))

            r, c = nr, nc

    # 오일러 다면체 정리(2차원) 사용
    # v - e + f = 1
    v = len(node_visited)
    e = len(edge_visited) // 2  # 양방향 간선을 고려헀으므로 반으로 나눠줌
    f = e - v + 1

    return f


print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([6, 5, 2, 7, 1, 4, 2, 4, 6]))
print(solution([5, 2, 7, 1, 6, 3]))
print(solution([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))

print(solution2([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution2([6, 5, 2, 7, 1, 4, 2, 4, 6]))
print(solution2([5, 2, 7, 1, 6, 3]))
print(solution2([6, 2, 4, 0, 5, 0, 6, 4, 2, 4, 2, 0]))
