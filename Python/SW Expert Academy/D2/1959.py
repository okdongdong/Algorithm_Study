# 1959. 두 개의 숫자열

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        long, short = A, B
    else:
        long, short = B, A
    max_num_sum = -99999999         # 이거보단 크겟지?
    for i in range(abs(N - M)+1):   # 두 문자열의 길이 차이 + 1 만큼의 경우의 수가 존재함, 0 1 2 / 1 2 이면 2가지 경우 존재
        num_sum = 0                 
        for j in range(min(N, M)):  # 짧은 숫자열의 길이만큼 반복해서 합 구함
            num_sum += long[j+i] * short[j]

        if max_num_sum < num_sum:   # 최대값 도출
            max_num_sum = num_sum

    print('#{} {}'.format(tc, max_num_sum))
