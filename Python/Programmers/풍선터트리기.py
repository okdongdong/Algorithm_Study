def solution(a):

    N = len(a)

    # 0, N-1번째는 무조건 가능
    cnt = 2

    # 기준 위치 오른쪽에 있는 숫자 중 가장 작은 숫자 저장
    right_min_nums = [0] * N
    now_min_num = a[-1]
    for i in range(N-1, -1, -1):
        now_min_num = min(a[i], now_min_num)
        right_min_nums[i] = now_min_num

    # 기준 위치 왼쪽에 있는 숫자 중 가장 작은 숫자 저장하면서 탐색
    now_min_num = a[0]
    for i in range(1, N-1):
        now_min_num = min(a[i], now_min_num)

        # 양쪽보다 모두 크다면 무조건 터져야함
        if now_min_num < a[i] and right_min_nums[i] < a[i]:
            continue

        cnt += 1

    return cnt
