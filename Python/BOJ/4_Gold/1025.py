N, M = map(int, input().split())

nums = [list(input()) for _ in range(N)]
square_num_list = []


def square_check(num):
    if num**0.5 == int(num**0.5):
        square_num_list.append(num)


def create_num(R, C):
    num = ''
    i = 0
    while i < len(R) and i < len(C):
        r, c = R[i], C[i]
        num += nums[r][c]
        i += 1
    return int(num)


# 행의 공차 d_r 열의 공차 d_c
for d_r in range(1, N+1):
    for c in range(M):
        num = ''
        for r in range(0, N, d_r):
            num += nums[r][c]

        square_check(int(num))

        num = ''
        for r in range(N-1, -1, -d_r):
            num += nums[r][c]

        square_check(int(num))

for d_c in range(1, M+1):
    for r in range(N):
        num = ''
        for c in range(0, M, d_c):
            num += nums[r][c]

        square_check(int(num))

        num = ''
        for c in range(M-1, -1, -d_c):
            num += nums[r][c]

        square_check(int(num))

for d_c in range(1, M+1):
    for d_r in range(1, N+1):

        RC_list = [
            (range(0, N, d_r), range(0, M, d_c)),
            (range(N-1, -1, -d_r), range(0, M, d_c)),
            (range(0, N, d_r), range(M-1, -1, -d_c)),
            (range(N-1, -1, -d_r), range(M-1, -1, -d_c))
        ]

        for R, C in RC_list:
            num = create_num(R, C)
            square_check(num)

if square_num_list:
    print(max(square_num_list))
else:
    print(-1)
