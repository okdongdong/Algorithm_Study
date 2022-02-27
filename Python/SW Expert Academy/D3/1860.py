T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))

    people_time_cnt = [0] * 11112
    boong_cnt = 0
    boong_time = 0

    for p in people:
        people_time_cnt[p] += 1

    for p in people_time_cnt:
        if boong_time == M:
            boong_time = 0
            boong_cnt += K

        boong_cnt -= p
        if boong_cnt < 0:
            result = 'Impossible'
            break
        boong_time += 1

    else:
        result = 'Possible'

    print('#{} {}'.format(tc, result))
