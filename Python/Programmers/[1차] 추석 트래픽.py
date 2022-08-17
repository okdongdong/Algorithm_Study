from heapq import heappush, heappop


def cal_start_time(end_hours, end_minutes, end_seconds, end_milisec, period):
    # 초당 최대 처리량을 반영하기 위해 0.999초 더 빼줌
    temp, start_milisec = divmod(end_milisec - period - 999, 1000)
    temp, start_seconds = divmod(end_seconds + temp, 60)
    temp, start_minutes = divmod(end_minutes + temp, 60)
    start_hours = end_hours + temp

    return (start_hours, start_minutes, start_seconds, start_milisec)


def solution(lines):
    # [(시작시간, 종료시간)] 으로 변환
    N = len(lines)
    time_tuple_list = []
    for line in lines:
        _, end_time, period = line.split()

        end_time = end_time.split('.')
        end_time = tuple(map(int, (*end_time[0].split(':'), end_time[1])))

        period = round(float(period[:-1])*1000)
        # 1.001 * 1000 의경우 1001아닌 1000.9999999로 계산되므로 round사용

        start_time = cal_start_time(*end_time, period)
        time_tuple_list.append((start_time, end_time))

    que = []

    # 시작순으로 다시 정렬
    time_tuple_list.sort()
    print(*time_tuple_list, sep='\n')

    for start_time, end_time in time_tuple_list:

        if que and que[0] <= start_time:
            # que[0] = earliest_end_time
            heappop(que)

        heappush(que, end_time)

    return len(que)


# def cal_time(input_hours, input_minutes, input_seconds, input_milisec, period):
#     temp, result_milisec = divmod(input_milisec + period, 1000)
#     temp, result_seconds = divmod(input_seconds + temp, 60)
#     temp, result_minutes = divmod(input_minutes + temp, 60)
#     result_hours = input_hours + temp

#     return (result_hours, result_minutes, result_seconds, result_milisec)


# def solution(lines):
#     # [(시작시간, 종료시간)] 으로 변환
#     N = len(lines)
#     time_tuple_list = []
#     for line in lines:
#         _, end_time, period = line.split()

#         end_time = end_time.split('.')
#         end_time = tuple(map(int, (*end_time[0].split(':'), end_time[1])))

#         period = round(float(period[:-1])*1000 - 1)

#         start_time = cal_time(*end_time, -period)
#         time_tuple_list.append((start_time, end_time))

#     max_cnt = 1
#     for i in range(N-1):
#         _, end_time = time_tuple_list[i]
#         end_range = cal_time(*end_time, 999)
#         cnt = 1
#         for j in range(i+1, N):
#             start_time, _ = time_tuple_list[j]
#             if start_time <= end_range:
#                 cnt += 1

#         max_cnt = max(max_cnt, cnt)

#     return max_cnt


print(solution([
    "2016-09-15 01:00:04.001 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))  # 1

print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))  # 2

print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))  # 7
