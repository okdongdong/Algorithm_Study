import sys
input = sys.stdin.readline

R, C = map(int, input().split())
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input())
sticks = list(map(int, input().split()))

is_left = True  # 왼쪽사람인지 오른쪽사람인지 판단

for stick in sticks:
    is_broken = False
    r = R - stick
    for c in range(C-1-(C-1)*is_left, (C+1)*is_left-1, 2*is_left-1):
        if cave[r][c] == 'x':
            cave[r][c] = '.'
            is_broken = True
            break

    is_left = not is_left

    if not is_broken:
        continue

    while True:
        check = [[0]*C for _ in range(R)]
        r = R-1
        for c in range(C):
            if cave[r][c] == 'x' and not check[r][c]:
                stack = [(r, c)]
                while stack:
                    rr, cc = stack.pop()
                    check[rr][cc] = 1
                    for dr, dc in drc:
                        nr, nc = rr+dr, cc+dc
                        if not(0 <= nr < R and 0 <= nc < C) or check[nr][nc] or cave[nr][nc] == '.':
                            continue

                        check[nr][nc] = 1
                        stack.append((nr, nc))

        cluster_cnt = 2
        clusters = [0, 0]
        for r in range(R):
            for c in range(C):
                cluster = []
                if cave[r][c] == 'x' and not check[r][c]:
                    stack = [(r, c)]
                    while stack:
                        rr, cc = stack.pop()
                        cluster.append((rr, cc))
                        check[rr][cc] = cluster_cnt
                        for dr, dc in drc:
                            nr, nc = rr+dr, cc+dc
                            if not(0 <= nr < R and 0 <= nc < C) or check[nr][nc] or cave[nr][nc] == '.':
                                continue

                            check[nr][nc] = cluster_cnt
                            stack.append((nr, nc))

                    clusters.append(cluster)
                    cluster_cnt += 1

        if cluster_cnt == 2:
            break

        for cnt in range(2, cluster_cnt):
            min_height = R

            for c in range(C):
                now_height = R
                upper_mineral = -1
                for r in range(R):
                    if cave[r][c] == '.':
                        continue

                    if check[r][c] == cnt:
                        upper_mineral = r

                    else:
                        if upper_mineral > -1:
                            now_height = r-upper_mineral-1
                            break

                else:
                    now_height = R - upper_mineral-1

                min_height = min(now_height, min_height)

            if min_height == R:
                continue

            for r, c in clusters[cnt]:
                cave[r][c] = '.'
                check[r][c] = 0

            for r, c in clusters[cnt]:
                cave[r+min_height][c] = 'x'
                check[r+min_height][c] = cnt

print('\n'.join(map(lambda x: ''.join(x), cave)))
