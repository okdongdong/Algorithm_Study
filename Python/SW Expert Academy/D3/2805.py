# 2805. 농작물 수확하기
# N은 항상 홀수

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    i = 0           # 마름모 모양으로 값을 추출하기 위한 인덱스 추가 값
    flag = True     # 인덱스 추가값의 증감을 제어하기 위한 flag
    profit = 0

    for r in range(N):
        for c in range(N//2-i,N//2 +1 +i):  # N//2: 중앙의 좌표
            profit += int(farm[r][c])

        if i == N//2:                       # 마름모에서 길이가 최대에 도달하면,
            flag = False                    # 다시 범위를 감소시키기 위해 flag 전환

        i = i + 1 if flag else i - 1        # flag가 True일 때 증가, False일 때 감소
    
    print('#{} {}'.format(tc, profit))

