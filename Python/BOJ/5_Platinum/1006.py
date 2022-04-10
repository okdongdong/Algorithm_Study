def check1():
    global cnt

    if (check[0][1] or wontagon[0][0] + wontagon[0][1] > W) and (check[1][0] or wontagon[0][0] + wontagon[1][0] > W):
        check[0][0] = True
        check[0][N] = True
        cnt += 1

    for i in range(1, N):
        if (check[0][i+1] or wontagon[0][i] + wontagon[0][i+1] > W) and (check[1][i] or wontagon[0][i] + wontagon[1][i] > W):
            check[0][i] = True
            cnt += 1

    if (check[1][1] or wontagon[1][0] + wontagon[1][1] > W):
        check[1][0] = True
        check[1][N] = True
        cnt += 1

    for i in range(1, N):
        if (check[1][i+1] or wontagon[1][i] + wontagon[1][i+1] > W):
            check[1][i] = True
            cnt += 1


def check2():
    global cnt

    if not (check[0][1] or wontagon[0][0] + wontagon[0][1] > W) and (check[1][0] or wontagon[0][0] + wontagon[1][0] > W):
        check[0][0] = True
        check[0][N] = True
        check[0][1] = True
        cnt += 1

    elif not (check[1][0] or wontagon[0][0] + wontagon[1][0] > W) and (check[0][1] or wontagon[0][0] + wontagon[0][1] > W):
        check[0][0] = True
        check[1][0] = True
        cnt += 1

    for i in range(1, N-1):
        if not (check[0][i+1] or wontagon[0][i] + wontagon[0][i+1] > W) and (check[1][i] or wontagon[0][i] + wontagon[1][i] > W):
            check[0][i] = True
            check[0][i+1] = True
            cnt += 1

        elif not (check[1][i] or wontagon[0][i] + wontagon[1][i] > W) and (check[0][i+1] or wontagon[0][i] + wontagon[0][i+1] > W):
            check[0][i] = True
            check[1][i] = True
            cnt += 1

    if not (check[1][1] or wontagon[1][0] + wontagon[1][1] > W):
        check[1][0] = True
        check[1][N] = True
        check[1][1] = True
        cnt += 1

    for i in range(1, N-1):
        if not (check[0][i+1] or wontagon[0][i] + wontagon[0][i+1] > W) and (check[1][i] or wontagon[0][i] + wontagon[1][i] > W):
            check[0][i] = True
            check[0][i+1] = True
            cnt += 1

        elif not (check[1][i] or wontagon[0][i] + wontagon[1][i] > W) and (check[0][i+1] or wontagon[0][i] + wontagon[0][i+1] > W):
            check[0][i] = True
            check[1][i] = True
            cnt += 1


T = int(input())

for tc in range(T):
    N, W = map(int, input().split())
    wontagon = [list(map(int, input().split())) for _ in range(2)]
    wontagon[0].append(wontagon[0][0])
    wontagon[1].append(wontagon[1][0])
    check = [[False]*(N+1) for _ in range(2)]
    cnt = 0
    pre_cnt = -1

    while cnt != pre_cnt:
        pre_cnt = cnt
        check1()
        # check2()

    division_idx_list = []
    for i in range(N):
        if check[0][i] and check[1][i]:
            division_idx_list.append[i]
    if len(division_idx_list) > 1:
        area_cnt = 0
        for k in range(2):
            for j in range(0, division_idx_list[0]):
                if not check[k][j]:
                    area_cnt += 1
            for j in range(division_idx_list[-1], N-1):
                if not check[k][j]:
                    area_cnt += 1
        cnt += (area_cnt+1)//2

        for i in range(len(division_idx_list)-1):
            area_cnt = 0
            for j in range(division_idx_list[i]+1, division_idx_list[i+1]):
                for k in range(2):
                    if not check[k][j]:
                        area_cnt += 1
            cnt += (area_cnt+1)//2

    else:
        area_cnt = 0
        for i in range(N):
            for j in range(2):
                if not check[j][i]:
                    area_cnt += 1
        cnt += (area_cnt+1)//2

print(cnt)
