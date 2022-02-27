import sys, pprint
input = sys.stdin.readline


def tornado(r, c, direction):
    global sand_out
    dr, dc = move_direction[direction]          # 진행방향
    dr2, dc2 = move_direction[(direction+1)%4]  # 진행방향의 왼쪽
    dr3, dc3 = move_direction[(direction+3)%4]  # 진행방향의 오른쪽
    spread_sand_list = [
        (r+dr2, c+dc2, 0.07), (r+dr+dr2, c+dc+dc2, 0.1), (r-dr+dr2, c-dc+dc2, 0.01), (r+2*dr2, c+2*dc2, 0.02),
        (r+dr3, c+dc3, 0.07), (r+dr+dr3, c+dc+dc3, 0.1), (r-dr+dr3, c-dc+dc3, 0.01), (r+2*dr3, c+2*dc3, 0.02),
        (r+2*dr, c+2*dc, 0.05)
    ]   # 흩날리는 지역과 비율
    
    # 흩날릴 모래양 
    now_sand = sands[r][c]
    alpha_sand = sands[r][c]
    sands[r][c] = 0
    
    # 비율이 적힌 칸에 대한 계산
    for tr, tc, ratio in spread_sand_list:
        alpha_sand -= int(now_sand * ratio)
        if 0 <= tr < N and 0 <= tc < N:
            sands[tr][tc] += int(now_sand * ratio)
        else:
            sand_out += int(now_sand * ratio)
    
    # alpha칸에 대한 계산
    if 0 <= r+dr < N and 0 <= c+dc < N:
        sands[r+dr][c+dc] += alpha_sand
    else:
        sand_out += alpha_sand

N = int(input())
sands = [list(map(int, input().split())) for _ in range(N)]
start = (N//2, N//2)
r, c = start
move_direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]    # 좌우하상
move_distance = 1   # 움직이는 거리, 방향전환 2번마다 한칸씩 더 움직임
move_flag = True
now_move_direction = 0
sand_out = 0
cnt = 1
while cnt < N**2-1:
    for i in range(move_distance):
        cnt += 1
        dr, dc = move_direction[now_move_direction]
        r += dr
        c += dc
        if not(0 <= r < N and 0 <= c < N):
            continue
        tornado(r, c, now_move_direction)
    # 두번의 방향전환 후에 이동거리가 하나씩 증가     
    if move_flag:
        move_flag = False
    else:
        move_distance += 1
        move_flag = True
    now_move_direction = (now_move_direction + 1)%4
    
print(sand_out)