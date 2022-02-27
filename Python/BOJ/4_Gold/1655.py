# 가운데를 말해요

import heapq
import sys
input = sys.stdin.readline

N = int(input())

mid = int(input())
small_list = []
big_list = []
result = [mid]
for _ in range(N-1):
    temp = int(input())
    if temp >= mid:
        if len(big_list) == len(small_list):
            heapq.heappush(big_list, temp)

        else:
            heapq.heappush(small_list, -mid)
            if big_list and big_list[0] < temp:
                mid = heapq.heappushpop(big_list, temp)
            else:
                mid = temp

    else:
        if len(big_list) > len(small_list):
            heapq.heappush(small_list, -1*temp)

        else:
            heapq.heappush(big_list, mid)
            if small_list and small_list[0] < -1 * temp:
                mid = -1 * heapq.heappushpop(small_list, -1 * temp)
            else:
                mid = temp

    result.append(mid)

print('\n'.join(map(str, result)))
