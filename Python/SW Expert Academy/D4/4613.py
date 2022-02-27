# 4613. 러시아 국기 같은 깃발

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    min_cnt = N * M

    for i in range(N-2):             # 하얀색을 칠하는 영역, i번쨰 행까지
        for j in range(i+1, N-1):    # 파란색을 칠하는 영역, j번째 행까지
            cnt = 0                  # 새로 칠해야하는 칸의 수
            for c in range(M):
                for r in range(i+1):        # 하얀색을 칠해야하는 칸의 수
                    if arr[r][c] != 'W':
                        cnt += 1
                for r in range(i+1, j+1):   # 파란색을 칠해야하는 칸의 수
                    if arr[r][c] != 'B':
                        cnt += 1
                for r in range(j+1, N):     # 빨간색을 칠해야하는 칸의 수
                    if arr[r][c] != 'R':
                        cnt += 1
            if min_cnt > cnt:         # 최솟값 비교
                min_cnt = cnt

    print('#{} {}'.format(tc, min_cnt))