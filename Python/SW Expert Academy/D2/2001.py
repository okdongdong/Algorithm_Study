# 2001. 파리 퇴치

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for c in range(N-M+1):      # 영역의 좌상단 좌표를 구함
        for r in range(N-M+1):
            kill = 0    

            for i in range(M):  # 좌상단 좌표부터 범위의 값을 구함
                for j in range(M):
                    kill += arr[r+i][c+j]

            if max_kill < kill: # 최대값 도출
                max_kill = kill

    print('#{} {}'.format(tc, max_kill))    