# 연구소
import copy

def virus():            # 바이러스가 퍼지게 하는 함수
    global min_virus_cnt

    virus_cnt = 0
    cnt = 0
    temp_virus_map = copy.deepcopy(virus_map)
    temp_virus_locations = virus_locations[:]
    while temp_virus_locations:
        r, c = temp_virus_locations.pop()
        for dr, dc in virus_drc:
            nr = r+dr
            nc = c+dc
            if 0 <= nr < N and 0 <= nc < M and temp_virus_map[nr][nc] == 0:
                temp_virus_map[nr][nc] = 2
                temp_virus_locations.append((nr, nc))
                virus_cnt += 1
                if virus_cnt > min_virus_cnt:
                    return False    # 바이러스의 최소 수 보다 많아지면 이미 가망이 없음

    if virus_cnt < min_virus_cnt:
        min_virus_cnt = virus_cnt

    for r in range(N):
        for c in range(M):
            if temp_virus_map[r][c] == 0:
                cnt += 1

    return cnt


def wall(_cnt):         # 벽을 세우는 함수
    global max_safe_area
    if _cnt == 3:       # 벽을 3개 세웠을 때 안전지대 수 카운트
        safe_area = virus()
        if safe_area and safe_area > max_safe_area:
            max_safe_area = safe_area
        return

    for r in range(N):
        for c in range(M):
            if _cnt > 0:                    # 벽을 하나도 세우지 않은 경우에는 근처에 벽이 없어도 벽을 세워야함
                for dr, dc in wall_drc:     # 벽 근처에다가 벽을 세워야 최대 안전지역을 확보할 수 있음
                    nr = r+dr
                    nc = c+dc
                    if 0 <= nr < N and 0 <= nc < M and virus_map[nr][nc] == 1:
                        break
                else:                       # 벽 근처가 아닌 경우 다른위치 탐색
                    continue

            if virus_map[r][c] == 0 and not visited[r][c]:
                if _cnt == 0:
                    visited[r][c] = True
                virus_map[r][c] = 1
                wall(_cnt + 1)
                virus_map[r][c] = 0


N, M = map(int, input().split())
virus_map = [list(map(int, input().split())) for _ in range(N)]
virus_drc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
wall_drc = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
visited = [[False]*M for _ in range(N)]
max_safe_area = 0
min_virus_cnt = N*M + 1
virus_locations = []

# virus count
for r in range(N):
    for c in range(M):
        if virus_map[r][c] == 2:
            virus_locations.append((r, c))

wall(0)

print(max_safe_area)
