# 로봇 청소기
def cleaning_robot(r, c, robot_direction):
    cleaning_cnt = 0
    while True:
        cleaning_cnt += 1
        rotation_cnt = 0
        visited[r][c] = True

        while True:
            if rotation_cnt == 4:   # 2-c.
                dr, dc = drc[robot_direction]
                r -= dr
                c -= dc
                if arr[r][c] == 1:  # 2-d.
                    return cleaning_cnt
                rotation_cnt = 0    # 2-c. 인경우 2번으로 돌아감

            next_direction = (robot_direction-1) % 4
            dr, dc = drc[next_direction]

            nr = r + dr
            nc = c + dc

            if arr[nr][nc] == 0 and not visited[nr][nc]:    # 2-a. 청소를 해야하는 곳이라면
                is_wall = False

            else:        # 2-b. 왼쪽이 벽 또는 이미 청소한 곳이라면
                is_wall = True

            if is_wall:  # 2-b.
                robot_direction = next_direction
                rotation_cnt += 1
                continue

            # 2-a.
            r += dr
            c += dc
            robot_direction = next_direction
            break


N, M = map(int, input().split())
r, c, robot_direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

print(cleaning_robot(r, c, robot_direction))
