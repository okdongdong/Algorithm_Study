def rotate_square(sr, sc):
    temp = [arr[r][sc : sc + N // 2] for r in range(sr, sr + N // 2)]

    for r in range(N // 2):
        for c in range(N // 2):
            arr[sr + r][sc + c] = temp[N // 2 - 1 - c][r]


def rotate_cross():
    temp = arr[N // 2][:]

    for i in range(N):
        arr[N // 2][i] = arr[i][N // 2]

    for i in range(N):
        arr[i][N // 2] = temp[N - 1 - i]


def get_groups():
    groups = []
    visited = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            visited[r][c] = True
            group_num = arr[r][c]
            group_cnt = 1
            group_edges = {}
            stack = [(r, c)]
            while stack:
                _r, _c = stack.pop()
                for dr, dc in drc:
                    nr, nc = _r + dr, _c + dc
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue

                    if arr[nr][nc] != group_num:
                        group_edges[arr[nr][nc]] = group_edges.get(arr[nr][nc], 0) + 1
                        continue

                    if visited[nr][nc]:
                        continue

                    visited[nr][nc] = True
                    stack.append((nr, nc))
                    group_cnt += 1

            groups.append([group_num, group_cnt, group_edges])

    return groups


def cal_score(groups):
    score = 0
    for num, cnt, edges in groups:
        for other_num, edge_cnt in edges.items():
            score += num * cnt * other_num * edge_cnt

    return score


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
drc = [(0, 1), (-1, 0), (0, -1), (1, 0)]
squares = [(0, 0), (0, N // 2 + 1), (N // 2 + 1, 0), (N // 2 + 1, N // 2 + 1)]
score = cal_score(get_groups())

for _ in range(3):
    for sr, sc in squares:
        rotate_square(sr, sc)
    rotate_cross()
    score += cal_score(get_groups())

print(score)
