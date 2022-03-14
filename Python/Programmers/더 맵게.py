import heapq


def solution(scoville, K):

    scoville.sort()

    cnt = 0
    while len(scoville) > 1:
        lowest_scoville_food = heapq.heappop(scoville)
        if lowest_scoville_food >= K:
            break

        second_low_scoville_food = heapq.heappop(scoville)

        mixed_food = lowest_scoville_food + second_low_scoville_food*2
        heapq.heappush(scoville, mixed_food)

        cnt += 1

    else:   # 모든음식을 섞어도 K가 안넘는 경우
        if mixed_food < K:
            cnt = -1

    return cnt


print(solution([1, 2, 3, 9, 10, 12],	7))
