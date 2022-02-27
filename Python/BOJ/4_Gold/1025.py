N, M = map(int, input().split())

nums = [list(input()) for _ in range(N)]

square_num = [i**2 for i in range(3163)]    # 9자리까지의 모든 제곱수
square_num_list = []

# 행의 공차 d_r 열의 공차 d_C
for d_c in range(1, M):
    for d_r in range(1, N):
        num = ''
        for r in range(0, N, d_r):
            for c in range(0, M, d_c):
                num += nums[r][c]
        num = int(num)
        if num**0.5 == int(num**0.5):
            square_num_list.append(num)

        num = ''
        for c in range(0, M, d_c):
            for r in range(N-1, -1, -d_r):
                num += nums[r][c]
        num = int(num)
        if num**0.5 == int(num**0.5):
            square_num_list.append(num)

        num = ''
        for r in range(N-1, -1, -d_r):
            for c in range(0, M, d_c):
                num += nums[r][c]
        num = int(num)
        if num**0.5 == int(num**0.5):
            square_num_list.append(num)

        num = ''
        for c in range(M-1, -1, -d_c):
            for r in range(N-1, -1, -d_r):
                num += nums[r][c]
        num = int(num)
        if num**0.5 == int(num**0.5):
            square_num_list.append(num)
        

# d_r = 0
# for d_c in range(1, M):
#     for r in range(0, N, d_r):
#         for c in range(0, M, d_c):
#             num += nums[r][c]
#     num = int(num)
#     if num**0.5 == int(num**0.5):
#         square_num_list.append(num)

#     num = ''
#     for c in range(0, M, d_c):
#         for r in range(N-1, -1, -d_r):
#             num += nums[r][c]
#     num = int(num)
#     if num**0.5 == int(num**0.5):
#         square_num_list.append(num)

#     num = ''
#     for r in range(N-1, -1, -d_r):
#         for c in range(0, M, d_c):
#             num += nums[r][c]
#     num = int(num)
#     if num**0.5 == int(num**0.5):
#         square_num_list.append(num)

#     num = ''
#     for c in range(M-1, -1, -d_c):
#         for r in range(N-1, -1, -d_r):
#             num += nums[r][c]
#     num = int(num)
#     if num**0.5 == int(num**0.5):
#         square_num_list.append(num)
# d_c = 0
# for d_r in range(1, N):
#     num = ''
#     for r in range(0, N, d_r):
#         for c in range(0, M, d_c):
#             num += nums[r][c]
#     num = int(num)
#     if num**0.5 == int(num**0.5):
#         square_num_list.append(num)

#     num = ''
#     for c in range(0, M, d_c):
#         for r in range(N-1, -1, -d_r):
#             num += nums[r][c]
#     num = int(num)
#     if num**0.5 == int(num**0.5):
#         square_num_list.append(num)

#     num = ''
#     for r in range(N-1, -1, -d_r):
#         for c in range(0, M, d_c):
#             num += nums[r][c]
#     num = int(num)
#     if num**0.5 == int(num**0.5):
#         square_num_list.append(num)

#     num = ''
#     for c in range(M-1, -1, -d_c):
#         for r in range(N-1, -1, -d_r):
#             num += nums[r][c]
#     num = int(num)
#     if num**0.5 == int(num**0.5):
#         square_num_list.append(num)

    # 완전제곱수 검사
print(max(square_num_list))