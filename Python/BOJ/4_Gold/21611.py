# 마법사 상어와 블리자드

# 방향: 상하좌우 / 1234
# 구슬 1, 2, 3번
# N은 항상 홀수

from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
magic_d_s_list = [list(map(int, input().split())) for _ in range(M)]
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상
ball_list = deque()
scores = [0] * 4
shark_rc = N // 2

# 소용돌이 좌표 생성
matrix = [[0] * N for _ in range(N)]
num = N ** 2 - 2  # 구슬리스트의 인덱스로 사용
direction = 0
r, c = 0, -1
while num > -1:
    dr, dc = drc[direction]
    nr = r + dr
    nc = c + dc
    if 0 <= nr < N and 0 <= nc < N and not matrix[nr][nc]:
        matrix[nr][nc] = num
        if arr[nr][nc]:
            ball_list.appendleft(arr[nr][nc])  # 구슬리스트에 추가
        r, c = nr, nc
        num -= 1

    else:
        direction = (direction + 1) % 4

# 마~법
drc = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]  # 0상하좌우
for d, s in magic_d_s_list:
    del_list = set()

    dr, dc = drc[d]
    for i in range(1, s + 1):
        del_list.add(matrix[shark_rc + dr * i][shark_rc + dc * i])

    # 구슬 폭발 / 그때 그때 없애주면 안됨
    temp = [[0, 0]]
    for i in range(len(ball_list)):
        if i in del_list:
            continue

        if temp[-1][1] == ball_list[i]:
            temp[-1][0] += 1
        else:
            temp.append([1, ball_list[i]])  # cnt, ball_num

    check = [False]*(N**2)
    flag = True
    while flag:
        flag = False
        pre_idx = 0
        for i in range(1, len(temp)):
            if check[i]:
                continue

            if not check[pre_idx] and temp[pre_idx][1] == temp[i][1]:
                temp[pre_idx][0] += temp[i][0]
                check[i] = True
                continue

            cnt, ball_num = temp[i]
            if cnt >= 4:
                flag = True
                check[i] = True
                scores[ball_num] += cnt
                continue
            
            pre_idx = i

    # 구슬 복제
    ball_list = []
    for i in range(1, len(temp)):
        if check[i]:
            continue
        ball_list += temp[i]
        if len(ball_list) == N**2 - 1:
            break

result = 0
for i in range(1, 4):
    result += i * scores[i]

print(result)
