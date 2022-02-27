# 파괴되지 않은 건물

# def solution(board, skill):
#     attack = []
#     heal = []
#     result = 0

#     for i in range(len(skill)):
#         if skill[i][0] == 1:
#             attack.append(i)
#         else:
#             heal.append(i)

#     for r in range(len(board)):
#         for c in range(len(board[0])):
#             temp = 0
#             for i in heal:
#                 if skill[i][1] <= r <= skill[i][3] and skill[i][2] <= c <= skill[i][4]:
#                     temp += skill[i][5]

#             board[r][c] += temp

#             for i in attack:
#                 if skill[i][1] <= r <= skill[i][3] and skill[i][2] <= c <= skill[i][4]:
#                     board[r][c] -= skill[i][5]
#                     if board[r][c] < 1:
#                         break
#             else:
#                 result += 1

#     return result


def solution(board, skill):
    N, M = len(board), len(board[0])

    # 누적합을 표현해놓을 배열 생성
    temp_arr = [[0]*(M+1) for _ in range(N+1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1

        # 누적합관련 정보 표시
        temp_arr[r1][c1] += degree
        temp_arr[r1][c2+1] -= degree
        temp_arr[r2+1][c1] -= degree
        temp_arr[r2+1][c2+1] += degree

    # 가로 계산
    for r in range(N):
        for c in range(1, M):
            temp_arr[r][c] += temp_arr[r][c-1]

    # 세로 계산
    for r in range(1, N):
        for c in range(M):
            temp_arr[r][c] += temp_arr[r-1][c]

    # 파괴되지 않은 건물 수 카운트
    result = 0
    for r in range(N):
        for c in range(M):
            if board[r][c]+temp_arr[r][c] > 0:
                result += 1

    return result


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
skill = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
print(solution(board, skill))
