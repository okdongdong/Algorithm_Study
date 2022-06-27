from heapq import heapify, heappop, heappush


def solution(n, works):
    works_heap = list(map(lambda x: x*-1, works))
    heapify(works_heap)
    for _ in range(n):
        temp = heappop(works_heap)
        if temp == 0:
            break

        temp += 1
        heappush(works_heap, temp)

    answer = 0
    for work in works_heap:
        answer += work ** 2

    return answer
