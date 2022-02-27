T = int(input())
for _ in range(T):
    W, N = map(int, input().split())
    x = [0] * N
    w = [0] * N
    distance = 0                 # 테스트 케이스 마다 distance와
    W_capacity = W               # 쓰레기 잔여용량을 초기화 해줘야 함
 
    for i in range(N):           # 각 지점의 거리와 쓰레기 양을 저장
        x[i], w[i] = map(int, input().split())

    i = 0                        # i : 지점 인덱스
    while i < N:
        if W_capacity == w[i]:   # 쓰레기 양이 용량에 도달한 경우, case 1
            distance += 2 * x[i]
            i += 1
            W_capacity = W       # case 2 이후 case 1이 발생한 경우 W_capacity 를 초기화 해줘야함

        elif W_capacity > w[i]:  # 쓰레기 양이 용량보다 작아 다음 지점으로 진행하는 경우, case 2
            W_capacity -= w[i]   # 용량이 다 차지 않을 경우 남은 용량 계산
            i += 1               # 다음지점으로 진행

        else:
            distance += 2 * x[i] # 실을 수 있는 용량 보다 많은 경오 다시 돌아깄다 와야하므로,
            W_capacity = W       # 거리는 추가 되고, 잔여용량 초기화, 인덱스는 유지

    if W_capacity < W:           # 마지막 지점에서 쓰래기를 가득 채우지 않고 돌아온 경우
        distance += 2 * x[N-1]

    print(distance)              # 모든 지점을 다 돈 뒤에 distance 출력