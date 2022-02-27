# 인구 이동
import sys
input = sys.stdin.readline

def find_not_visited(rs, cs):
    for _r in range(rs, N):     # DFS가 끝난 좌표부터 방문안한 지점 탐색
        for _c in range(cs, N):
            if visited[_r][_c] < 0:
                return _r, _c

    for _r in range(N):
        for _c in range(N):
            if visited[_r][_c] < 0:
                return _r, _c


N, L, R = map(int, input().split())
nation = [list(map(int, input().split())) for _ in range(N)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]    # 북서동남
day = 0

while True:
    stack = [[] for _ in range(N**2)]
    visited = [[-1]*N for _ in range(N)]
    border_num = 0
    rs, cs = 0, 0


    # 국경선 오픈여부 판별
    while True:
        try:    # 국경선이 연결되지 않은 지역을 찾아서 탐색해준다.
            r, c = find_not_visited(rs, cs)
        except:
            break

        stack[border_num].append((r, c))
        temp=[(r, c)]
        while temp:  # DFS방식으로 주변 탐색
            r, c = temp.pop()
            visited[r][c] = border_num
            for dr, dc in drc:
                nr = r+dr
                nc = c+dc
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] < 0:
                    if L <= abs(nation[nr][nc] - nation[r][c]) <= R:
                        stack[border_num].append((nr, nc))  # 국경선 번호별로 추가해줌
                        temp.append((nr, nc))
                        visited[nr][nc] = border_num
        rs, cs = r, c
        border_num += 1

    # 인구이동
    if stack[-1]:   # stack의 마지막까지 가득 찬 경우 == 인구이동이 없는 경우
        break

    for nation_list in stack:
        if len(nation_list) == 0:
            break

        if len(nation_list) == 1:
            continue

        total_population = 0
        for nation_r, nation_c in nation_list:
            total_population += nation[nation_r][nation_c]
        population = total_population//len(nation_list)

        for nation_r, nation_c in nation_list:
            nation[nation_r][nation_c] = population

    day += 1

print(day)
