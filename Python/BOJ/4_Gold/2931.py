# 가스관

R, C = map(int, input().split())
arr = [input() for _ in range(R)]
pre_direction = {
    '|': set([(-1, 0), (1, 0)]),
    '-': set([(0, -1), (0, 1)]),
    '1': set([(-1, 0), (0, -1)]),
    '2': set([(1, 0), (0, -1)]),
    '3': set([(1, 0), (0, 1)]),
    '4': set([(-1, 0), (0, 1)]),
    'M': set(),
    'Z': set()  # 키에러 방지
}

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start_rc = 0

# 모스크바의 위치를 찾음
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'M':
            start_rc = (r, c)
            break
    if start_rc:
        break

# 시작위치에서 갈 수 있는 방향을 탐색
r, c = start_rc
for dr, dc in drc:
    nr, nc = r+dr, c+dc
    if not(0 <= nr < R and 0 <= nc < C):
        continue

    if (arr[nr][nc] != '.') and ((dr, dc) in pre_direction[arr[nr][nc]]):
        r, c = nr, nc
        pre_drc = (dr, dc)
        break

# 중단된 지점이 나올때까지 탐색
while arr[r][c] != '.':

    for dr, dc in pre_direction[arr[r][c]]:
        if pre_drc == (dr, dc):
            continue
        pre_drc = (-dr, -dc)
        r -= dr
        c -= dc
        if arr[r][c] == '+':
            r -= dr
            c -= dc
        break

# 중단점에서 사방을 탐색
direction_cnt = 0
for dr, dc in drc:
    if pre_drc == (-dr, -dc):
        continue
    nr, nc = r+dr, c+dc
    if not(0 <= nr < R and 0 <= nc < C):
        continue

    if arr[nr][nc] == '+' or (arr[nr][nc] != '.' and (dr, dc) in pre_direction[arr[nr][nc]]):

        direction_cnt += 1
        next_drc = (-dr, -dc)

# 사방으로 갈 수있는 길이 두개이상이면 +
if direction_cnt > 1:
    block = '+'
else:
    for idx, vals in pre_direction.items():
        if pre_drc in vals and next_drc in vals:
            block = idx
            break

print(r+1, c+1, block)
