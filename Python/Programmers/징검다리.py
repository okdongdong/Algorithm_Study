def solution(distance, rocks, n):

    rocks.sort()

    # 돌 사이 간격 계산
    rock_distance = [rocks[0]]
    for i in range(1, len(rocks)):
        rock_distance.append(rocks[i] - rocks[i-1])
    rock_distance.append(distance - rocks[-1])

    left, right = 0, distance

    while left < right:
        mid = (left+right) >> 1

        delete_cnt = 0
        temp_distance = 0
        for dist in rock_distance:
            temp_distance += dist
            if temp_distance > mid:
                temp_distance = 0
            else:
                delete_cnt += 1

        if delete_cnt > n:
            right = mid
        else:
            left = mid + 1

    return left


print(solution(	25, [2, 14, 11, 21, 17], 2))
