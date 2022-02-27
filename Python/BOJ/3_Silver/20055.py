# 컨베이어 벨트 위의 로봇

N, K = map(int, input().split())
belts = list(map(int, input().split()))
NN = 2*N
robots_on_belt = [False]*NN
check = [True]*NN
next_robot = 1
robot_move = 0

load = 0
unload = N-1
step = 0
cnt = 0

while cnt < K:
    step += 1
    # 벨트 회전
    load = (load - 1) % NN
    unload = (unload - 1) % NN

    # 로봇 이동
    robots_on_belt[unload] = False
    for i in range(N-1):
        idx = (unload - i) % NN
        pre_idx = (unload - i - 1) % NN
        if belts[idx] > 0 and check[idx] and not robots_on_belt[idx]:
            if robots_on_belt[pre_idx]:

                robots_on_belt[pre_idx] = False
                robots_on_belt[idx] = True

                belts[idx] -= 1
                if belts[idx] == 0:
                    check[idx] = False
                    cnt += 1
            robots_on_belt[unload] = False

    # 로봇 올리기
    if check[load]:
        robots_on_belt[load] = True
        belts[load] -= 1
        if belts[load] == 0:
            check[load] = False
            cnt += 1

print(step)