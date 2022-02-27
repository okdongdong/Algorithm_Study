# 농장 관리

def is_top(r, c):   # 현재위치의 높이의 집합이 봉우리인지 확인
    now_height = farm[r][c]
    stack = [(r, c)]
    flag = True
    while stack:
        r, c = stack.pop()
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and farm[nr][nc] == now_height:
                    stack.append((nr, nc))  # 인접한 동일 높이는 모두 탐색함
                    visited[nr][nc] = True
                elif farm[nr][nc] > now_height: # 인접한 격자 중에 현재보다 높은 곳이 존재할 경우 봉우리가 아니다
                    flag = False

    if flag:
        return True

    return False


N, M = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

drc = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cnt = 0
stack = []

for r in range(N):
    for c in range(M):
        if not visited[r][c] and is_top(r, c):
            cnt += 1

print(cnt)
