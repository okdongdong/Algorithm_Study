# 1954. 달팽이 숫자

drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 방향이 우-하-좌-상-우 로 순환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    r, i, num = 0, 0, 1
    c = -1  # (0,-1) 부터 시작
    while num <= N**2:
        dr, dc = drc[i]
        r += dr
        c += dc
        if 0<=r<N and 0<=c<N and not arr[r][c]:  # 조건에 맞으면, 값을 넣고 숫자를 1증가시킴
            arr[r][c] = num
            num += 1
        else:           # 범위를 벗어나거나, 값이 이미 존재하는 경우 방향 전환
            r -= dr     # 범위를 벗어나므로 다시 한칸 뒤로 후퇴
            c -= dc
            i = (i+1)%4 # 순환하는 방향 구현

    print('#{}'.format(tc))
    for i in range(N):
        print(*arr[i])
    