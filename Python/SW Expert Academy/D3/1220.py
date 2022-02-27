# 1220. [S/W 문제해결 기본] 5일차 - Magnetic

# 위: N극, 아래: S극 / 1: N극, 2: S극
for tc in range(1, 11):     
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for c in range(N):
        flag = False
        for r in range(N):
            if table[r][c] == 1:
                flag = True

            elif table[r][c] == 2 and flag:
                flag = False
                cnt += 1

    print('#{} {}'.format(tc, cnt))