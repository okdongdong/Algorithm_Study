from heapq import heappush, heappop


def solution(jobs):
    N = len(jobs)
    jobs.sort(reverse=True)
    total_time = 0
    wait_time = 0
    que = []
    while que or jobs:
        if not que and jobs:
            heappush(que, jobs.pop()[::-1])

        while jobs and jobs[-1][0] <= total_time:
            heappush(que, jobs.pop()[::-1])

        if que:
            period, request = heappop(que)
            wait_time += max(total_time - request, 0) + period
            total_time = max(request, total_time) + period

    result = wait_time//N

    return result


print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
print(solution([[0, 3], [5, 9], [4, 1], [8, 1]]))  # 9
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))  # 13
print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))  # 13
