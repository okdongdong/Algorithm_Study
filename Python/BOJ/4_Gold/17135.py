# 캐슬 디펜스

# 칸에는 적하나, 궁수하나씩만
# 궁수 3명
# 같은 거리인 경우 왼쪽 적 없앰

from itertools import combinations
from collections import deque

drc = [(0, -1), (-1, 0), (0, 1)]


def search(min_range, max_range, archer):
    r = N-1 - min_range
    c = archer
    visited = [[False]*M for _ in range(N)]
    visited[r][c] = True
    deq = deque([(r, c)])

    while deq:
        r, c = deq.popleft()
        if arrow_range_arr_list[archer][r][c] and not check[r][c]:
            if arrow_range_arr_list[archer][r][c] <= max_range:
                return (r, c)
            else:
                return False

        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                deq.append((nr, nc))


N, M, D = map(int, input().split())
enemy_arr = [list(map(int, input().split())) for _ in range(N)]
archer_placement_list = list(combinations(range(M), 3))
arrow_range_arr_list = [[[0]*M for _ in range(N)] for _ in range(M)]
max_kill_cnt = 0

# 궁수 위치별 적군과의 거리
for i in range(M):
    for r in range(N):
        for c in range(M):
            if enemy_arr[r][c]:
                arrow_range_arr_list[i][r][c] = abs(N-r) + abs(i-c)


# 모든 궁수위치에 대해 확인
for archer_placement in archer_placement_list:
    check = [[False]*M for _ in range(N)]
    kill_cnt = 0

    # 적군이 모두 들이닥칠 때까지 반복
    for i in range(N):
        temp_rc = set()
        for archer in archer_placement:
            temp_result = search(i, D + i, archer)
            if temp_result:
                r, c = temp_result
                temp_rc.add((r, c))

        kill_cnt += len(temp_rc)
        for r, c in temp_rc:
            check[r][c] = True

    max_kill_cnt = max(max_kill_cnt, kill_cnt)

print(max_kill_cnt)
