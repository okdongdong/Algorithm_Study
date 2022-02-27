# 운동

N, m, M, T, R = map(int, input().split())

time_cnt = 0
ex_time_cnt = 0
heart_beat = m
if m+T > M:
    time_cnt = -1

else:
    while ex_time_cnt < N:
        if heart_beat + T <= M:
            heart_beat += T
            ex_time_cnt += 1

        else:
            heart_beat = max(heart_beat-R, m)
        time_cnt += 1

print(time_cnt)
