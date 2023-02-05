M, N, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

for _ in range(K):
    xs, ys, xe, ye = map(int, input().split())

    for x in range(xs, xe):
        for y in range(ys, ye):
            arr[x][y] = 1

result = []
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for r in range(N):
    for c in range(M):
        if arr[r][c]:
            continue

        stack = [(r, c)]
        arr[r][c] = 1
        cnt = 0

        while stack:
            _r, _c = stack.pop()
            cnt += 1
            for dr, dc in drc:
                nr, nc = _r + dr, _c + dc
                if not (0 <= nr < N and 0 <= nc < M) or arr[nr][nc]:
                    continue

                stack.append((nr, nc))
                arr[nr][nc] = 1

        result.append(cnt)

result.sort()
print(len(result))
print(*result)
