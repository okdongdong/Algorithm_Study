def time_to_idx(t):

    h, m, s = map(int, t.split(':'))

    return h*3600 + m*60 + s


def idx_to_time(idx):

    t = ''
    temp, idx = divmod(idx, 3600)
    t += f'{temp:02.0f}:'
    temp, idx = divmod(idx, 60)
    t += f'{temp:02.0f}:{idx:02.0f}'

    return t


def solution(play_time, adv_time, logs):
    N = (time_to_idx(play_time)+1)
    time_list = [0] * N

    # 시청구간의 시작점과 끝점만 계산
    for log in logs:
        st, et = log.split('-')
        st_idx = time_to_idx(st)
        et_idx = time_to_idx(et)
        time_list[st_idx] += 1
        time_list[et_idx] -= 1

    # 해당순간의 시청 cnt 계산
    time_cnt_list = [0]*N
    temp_time = 0
    for i in range(N):
        time_cnt_list[i] = temp_time
        temp_time += time_list[i]

    # 구간의 크기가 일정하므로 그냥 투포인터쓸래
    adv_idx = time_to_idx(adv_time)
    temp_time = max_time = sum(time_cnt_list[:adv_idx+1])
    max_idx = 0

    for i in range(adv_idx+1, N):
        temp_time += time_cnt_list[i] - time_cnt_list[i-adv_idx]
        if temp_time > max_time:
            max_time = temp_time
            max_idx = i-adv_idx

    result = idx_to_time(max_idx)

    return result


print(solution("02:03:55",	"00:14:15",	[
      "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("50:00:00",	"50:00:00",	[
      "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
