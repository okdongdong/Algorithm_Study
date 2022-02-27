# 주사위 굴리기
from collections import deque

N, M, r, c, K = map(int, input().split())
dice_map = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))
drc = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]  # 동서북남
dice_r = deque([0] * 4)
dice_c = deque([0] * 4)


result = []
i = 0
while i < K:
    dr, dc = drc[command[i]]
    i += 1

    if not (0 <= r + dr < N and 0 <= c + dc < M):
        continue

    r += dr
    c += dc

    if dr:
        if dr > 0:
            num = dice_r.pop()
            dice_r.appendleft(num)
            
        else:
            num = dice_r.popleft()
            dice_r.append(num)
            
        dice_c[1] = dice_r[1]
        dice_c[3] = dice_r[3]
        result.append(dice_r[3])

    else:
        if dc > 0:
            num = dice_c.pop()
            dice_c.appendleft(num)
            
        else:
            num = dice_c.popleft()
            dice_c.append(num)

        dice_r[1] = dice_c[1]
        dice_r[3] = dice_c[3]
        result.append(dice_c[3])
    
    if dice_map[r][c]:
        dice_r[1] = dice_map[r][c]
        dice_c[1] = dice_map[r][c]
        dice_map[r][c] = 0
    else:
        dice_map[r][c] = dice_r[1]

print(*result, sep='\n')
