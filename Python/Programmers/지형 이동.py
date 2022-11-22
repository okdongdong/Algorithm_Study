def solution(land, height):
    N = len(land)
    drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    arr = [[0] * N for _ in range(N)]

    group_num = 1
    boundary = set()

    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                continue

            stack = [(r, c)]
            while stack:
                _r, _c = stack.pop()
                arr[_r][_c] = group_num
                for dr, dc in drc:
                    nr, nc = _r + dr, _c + dc
                    if not (0 <= nr < N and 0 <= nc < N) or arr[_r][_c] == arr[nr][nc]:
                        continue

                    if abs(land[nr][nc] - land[_r][_c]) > height:
                        (r1, c1), (r2, c2) = sorted([(_r, _c), (nr, nc)])
                        boundary.add((abs(land[nr][nc] - land[_r][_c]), r1, c1, r2, c2))

                    else:
                        stack.append((nr, nc))

            group_num += 1

    head = list(range(group_num))

    def find_head(n):
        if head[n] != n:
            head[n] = find_head(head[n])
        return head[n]

    def union(a, b):
        head_a = find_head(a)
        head_b = find_head(b)
        head[head_b] = head_a

    boundary = sorted(boundary)
    answer = 0

    for diff, r1, c1, r2, c2 in boundary:
        head1 = find_head(arr[r1][c1])
        head2 = find_head(arr[r2][c2])

        if head1 == head2:
            continue

        answer += diff
        union(head1, head2)

    return answer


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
