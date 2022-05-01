# 다리 만들기
from collections import deque

drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def check_area(sr, sc):
    que = deque([(sr, sc)])
    visited[sr][sc] = True
    boundary = set()
    while que:
        r, c = que.popleft()
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if not(0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
                continue

            if island[nr][nc]:
                visited[nr][nc] = True
                que.append((nr, nc))
            else:
                boundary.add((nr, nc))

    return boundary


def cal_distance(boundary):
    boundary = list(boundary)
    temp_visited = [[False]*N for _ in range(N)]
    for r, c in boundary:
        temp_visited[r][c] = True

    distance = 1
    flag = False
    while boundary:
        temp = []
        for r, c in boundary:
            for dr, dc in drc:
                nr, nc = r+dr, c+dc
                if not(0 <= nr < N and 0 <= nc < N) or temp_visited[nr][nc] or visited[nr][nc]:
                    continue

                if island[nr][nc]:
                    flag = True
                    continue

                temp_visited[nr][nc] = True
                temp.append((nr, nc))

        if flag:
            return distance

        distance += 1
        boundary = temp

    return 987654321


N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
min_distance = 987654321
for r in range(N):
    for c in range(N):
        if not visited[r][c] and island[r][c]:
            min_distance = min(min_distance, cal_distance(check_area(r, c)))

print(min_distance)
