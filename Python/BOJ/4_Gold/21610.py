# 마법사 상어와 비바라기

N, M = map(int, input().split())
A_arr = [list(map(int, input().split())) for _ in range(N)]
d_s = [list(map(int, input().split())) for _ in range(M)]
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
drc = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
cloud = set([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

for d, s in d_s:
    temp = set()
    while cloud:
        r, c = cloud.pop()
        r = (r+s*dr[d]) % N
        c = (c+s*dc[d]) % N
        A_arr[r][c] += 1
        temp.add((r, c))

    for r, c in temp:
        cnt = 0
        for _dr, _dc in drc:
            nr = r+_dr
            nc = c+_dc
            if 0 <= nr < N and 0 <= nc < N and A_arr[nr][nc]:
                cnt += 1
        A_arr[r][c] += cnt

    cloud = set()
    for r in range(N):
        for c in range(N):
            if A_arr[r][c] >= 2 and (r, c) not in temp:
                A_arr[r][c] -= 2
                cloud.add((r, c))

print(sum(map(sum, A_arr)))
