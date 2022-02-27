N, L = map(int, input().split())

distance = 0
time = 0
pre_D = 0

for i in range(N):
    D, R, G = map(int, input().split())
    time += D - pre_D       # 총 이동 시간
    distance += D - pre_D   # 총 이동 거리
    pre_D = D
    cycle = R + G           # 신호 한바퀴 주기

    if time % cycle < R:
        time += R - (time % cycle)
    
time += L - distance        # 마지막 위치에서 골인지점까지 시간
print(time)
