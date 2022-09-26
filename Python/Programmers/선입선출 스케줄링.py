def solution(n, cores):
    if n-len(cores) <= 0:
        return n

    min_time = 0
    max_time = 250000000

    while min_time < max_time:
        now_time = (min_time+max_time)//2
        task_cnt = 0
        for core in cores:
            task_cnt += now_time//core + 1

        if task_cnt >= n:
            max_time = now_time
        else:
            min_time = now_time+1

    task_cnt = sum(map(lambda x: (max_time-1)//x + 1, cores))
    for idx, core in enumerate(cores):
        if not max_time % core:
            task_cnt += 1
            if task_cnt == n:
                return idx+1


print(solution(6, [1, 2, 3]))


# from heapq import heappush, heappop

# # 효율성 실패
# def solution(n, cores):
#     # 남은시간, 코어의 번호, 코어의 작업처리 시간
#     core_remain_time = list(
#         map(list, zip([0]*len(cores), range(1, len(cores)+1), cores))
#     )
#     last_core = 0
#     task_cnt = 0

#     while task_cnt < n:
#         task_cnt += 1
#         core_time, core_idx, core_work_time = heappop(core_remain_time)
#         last_core = core_idx
#         heappush(core_remain_time, [
#             core_time + core_work_time, core_idx, core_work_time
#         ])

#     return last_core
