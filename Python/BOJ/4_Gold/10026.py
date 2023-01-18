N = int(input())
arr = [input() for _ in range(N)]
drc = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def solution(diff_colors):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            cnt += 1
            visited[r][c] = 1
            color = arr[r][c]
            stack = [(r, c)]
            while stack:
                _r, _c = stack.pop()
                for dr, dc in drc:
                    nr, nc = _r + dr, _c + dc
                    if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc] or arr[nr][nc] in diff_colors[color]:
                        continue

                    visited[nr][nc] = 1
                    stack.append((nr, nc))

    return cnt


diff_colors1 = {"R": set(("G", "B")), "G": set(("R", "B")), "B": set(("R", "G"))}
diff_colors2 = {"R": set(("B")), "G": set(("B")), "B": set(("R", "G"))}

print(solution(diff_colors1), solution(diff_colors2))
