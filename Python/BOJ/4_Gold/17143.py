# 낚시왕

# 1. 낚시왕 이동
# 2. 낚시왕이 상어를 잡음
# 3. 상어이동
# 4. 상어가 겹치면 가장 큰상어가 다른놈들 먹음
# 좌상단 (1,1)부터 시작
# 방향 1~4 : 상하우좌
# 상어의 크기와 시작위치는 모두 다름
# 낚시왕이 오른쪽 끝에 도착했을 때 잡은 상어 크기의 합 출력

R, C, M = map(int, input().split())
direction = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]
sharks_info_list = {}    # 크기 : [r, c, dr, dc]
arr = [[0]*C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = list(map(int, input().split()))  # r, c, 속력, 방향, 크기
    r -= 1
    c -= 1
    dr, dc = direction[d]
    dr *= s
    dc *= s
    arr[r][c] = z
    sharks_info_list[z] = [r, c, dr, dc]

result = 0
for king in range(C):   # 낚시왕 이동
    # 상어 잡음
    for r in range(R):
        if arr[r][king]:
            z = arr[r][king]
            arr[r][king] = 0

            del sharks_info_list[z]
            result += z
            break

    # 상어이동
    next_shark = {}
    del_list = []
    for z, (r, c, dr, dc) in sharks_info_list.items():
        arr[r][c] = 0
        nr = r + dr
        nc = c + dc
        
        while not (0 <= nr < R and 0 <= nc < C):
            if nr >= R:
                nr = 2*(R-1) - nr
            elif nr < 0:
                nr *= -1
            elif nc >= C:
                nc = 2*(C-1) - nc
            else:
                nc *= -1

            dr *= -1    # 방향전환
            dc *= -1

        try:    # 겹치면 잡아먹힘
            if next_shark[(nr, nc)] < z:
                del_list.append(next_shark[(nr, nc)])
                next_shark[(nr, nc)] = z
            else:
                del_list.append(z)
        except:
            next_shark[(nr, nc)] = z

        sharks_info_list[z] = [nr, nc, dr, dc]

    # 잡아먹힌 상어 제거
    for z in del_list:
        del sharks_info_list[z] 

    # 배열에 상어 크기 다시 표시
    for (r, c), z in next_shark.items():
        arr[r][c] = z
    
print(result)