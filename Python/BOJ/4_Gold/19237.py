# 어른 상어
import sys
input = sys.stdin.readline

N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sharks_directions = [0] + list(map(int, input().split()))
direction_priority_list = [[[] for _ in range(5)] for _ in range(M+1)]
drc = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
k += 1          # 냄새 계산 편의를 위해 1추가
shark_cnt = M   # 상어 수
dead_shark_list = [False] * (M+1)

# 각 상어별 방향 우선순위 저장
for shark_num in range(1, M+1):
    for direction in range(1, 5):
        direction_priority_list[shark_num][direction] = list(map(int, input().split()))

sharks_rc = [0] * (M+1)
smell_dict = {}
for r in range(N):
    for c in range(N):
        if board[r][c]:
            smell_dict[(r, c)] = [board[r][c], k]
            sharks_rc[board[r][c]] = [r,c]

time_cnt = 0
while shark_cnt > 1:
    # del_smell
    del_list = []
    for (r, c) in smell_dict.keys():
        if smell_dict[(r, c)][1] == 1:
            del_list.append((r, c))
            continue

        smell_dict[(r, c)][1] -= 1

    for key in del_list:
        del smell_dict[key]

    # shark_move
    add_list = []
    for shark_num in range(1, M+1):
        if dead_shark_list[shark_num]:
            continue

        r, c = sharks_rc[shark_num]
        board[r][c] = 0
        direction_priority = direction_priority_list[shark_num][sharks_directions[shark_num]]
        temp_rc = 0
        for i in direction_priority:
            nr = r + drc[i][0]
            nc = c + drc[i][1]
            if not (0<=nr<N and 0<=nc<N):
                continue

            if smell_dict.get((nr, nc)):
                if smell_dict[(nr, nc)][0] == shark_num and not temp_rc:
                    temp_rc = (nr, nc)
                    idx = i
            else:
                if board[nr][nc]:  # 무조건 작은 번호부터 움직이므로 있기만 하면 죽여야함
                    dead_shark_list[shark_num] = True
                    shark_cnt -= 1
                    break 
                
                board[nr][nc] = shark_num
                sharks_rc[shark_num] = (nr, nc)
                add_list.append((shark_num, nr, nc))
                sharks_directions[shark_num] = i
                break
        
        else:
            r, c = temp_rc
            sharks_directions[shark_num] = idx
            sharks_rc[shark_num] = temp_rc
            add_list.append((shark_num, r, c))
            board[r][c] = shark_num

    # add_smell
    for shark_num, r, c in add_list:
        smell_dict[(r, c)] = [shark_num, k]

    time_cnt +=1
    if time_cnt > 1000:
        time_cnt = -1
        break

print(time_cnt)
