def solution(stones, k):

    min_cnt, max_cnt = 1, 200000000

    while min_cnt < max_cnt:
        now_cnt = (min_cnt + max_cnt)//2

        temp_cnt = 0
        for stone in stones:
            if stone <= now_cnt:
                temp_cnt += 1

                # 현재 친구들이 못 건넘
                if temp_cnt >= k:
                    max_cnt = now_cnt
                    break

                continue

            temp_cnt = 0

        else:
            # 현재 친구들이 모두 건널 수 있음
            min_cnt = now_cnt + 1

    return min_cnt


# # 효율성 X
# def solution(stones, k):
#     result = 200000001
#     N = len(stones)

#     for i in range(N-k+1):
#         result = min(result, max(stones[i:i+k]))
#     return result

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
