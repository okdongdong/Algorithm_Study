# 경사로

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
possible_road_cnt = 0

# 가로
for r in range(N):
    temp_cnt = 1
    is_go_up_possible = False
    is_go_down_possible = True
    for c in range(1, N):

        if abs(arr[r][c]-arr[r][c-1]) > 1:
            break

        if arr[r][c]-arr[r][c-1] == 0:
            temp_cnt += 1

        if temp_cnt >= L:
            if is_go_down_possible:
                is_go_up_possible = True
            else:
                temp_cnt -= L
            is_go_down_possible = True

        if arr[r][c]-arr[r][c-1] == -1:
            if is_go_down_possible:
                temp_cnt = 1
                is_go_down_possible = False
                is_go_up_possible = False
            else:
                break

        if arr[r][c]-arr[r][c-1] == 1:
            if is_go_up_possible:
                temp_cnt = 1
                is_go_up_possible = False
            else:
                break

    else:
        if is_go_down_possible or temp_cnt >= L:
            possible_road_cnt += 1

# 세로
for c in range(N):
    temp_cnt = 1
    is_go_up_possible = False
    is_go_down_possible = True
    for r in range(1, N):

        if abs(arr[r][c]-arr[r-1][c]) > 1:
            break

        if arr[r][c]-arr[r-1][c] == 0:
            temp_cnt += 1

        if temp_cnt >= L:
            if is_go_down_possible:
                is_go_up_possible = True
            else:
                temp_cnt -= L
            is_go_down_possible = True

        if arr[r][c]-arr[r-1][c] == -1:
            if is_go_down_possible:
                temp_cnt = 1
                is_go_down_possible = False
                is_go_up_possible = False
            else:
                break

        if arr[r][c]-arr[r-1][c] == 1:
            if is_go_up_possible:
                temp_cnt = 1
                is_go_up_possible = False
            else:
                break

    else:
        if is_go_down_possible or temp_cnt >= L:
            possible_road_cnt += 1

print(possible_road_cnt)
