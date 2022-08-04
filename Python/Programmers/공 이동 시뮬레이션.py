def solution(n, m, x, y, queries):

    dx = 0
    sr, sc = er, ec = x, y  # 좌상단, 우하단

    for i in range(len(queries)-1, -1, -1):
        command, temp_dx = queries[i]
        dx = temp_dx * (-1)**(command % 2)

        if sr > n-1 or er < 0 or sc > m-1 or ec < 0:
            return 0

        if command == 0:
            if sc > 0:
                sc += dx
            ec = min(ec+dx, m-1)

        elif command == 1:
            if ec < m-1:
                ec += dx
            sc = max(sc+dx, 0)

        elif command == 2:
            if sr > 0:
                sr += dx
            er = min(er+dx, n-1)

        else:
            if er < n-1:
                er += dx
            sr = max(sr+dx, 0)

    cnt = (er-sr+1) * (ec-sc+1)

    return cnt


print(solution(2, 3, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
print(solution(1000, 1000, 1, 1, [[0, 100001], [2, 100001]]))
print(solution(1000, 1000, 0, 0, [[0, 100001], [2, 1]]))
print(solution(1, 100, 0, 0, [[0, 100001], [1, 1]]))


# def solution(n, m, x, y, queries):

#     is_row = queries[0][0] > 1
#     dx = 0

#     sr, sc = er, ec = x, y  # 좌상단, 우하단

#     for i in range(len(queries)-1, -1, -1):
#         command, temp_dx = queries[i]

#         is_row = command > 1
#         dx = temp_dx * (-1)**(command % 2)

#         if is_row:
#             if dx > 0 and sr == 0:
#                 er = min(er+dx, n-1)

#             elif dx < 0 and er == n-1:
#                 sr = max(sr+dx, 0)

#             else:
#                 sr = max(sr+dx, 0)
#                 er = min(er+dx, n-1)

#         else:
#             if dx > 0 and sc == 0:
#                 ec = min(ec+dx, m-1)

#             elif dx < 0 and ec == m-1:
#                 sc = max(sc+dx, 0)

#             else:
#                 sc = max(sc+dx, 0)
#                 ec = min(ec+dx, m-1)

#     if sr > er or sc > ec:
#         return 0

#     cnt = (er-sr+1) * (ec-sc+1)

#     return cnt


# print(solution(2, 3, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
# print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
# print(solution(1000, 1000, 1, 1, [[0, 100001], [2, 100001]]))
# print(solution(1000, 1000, 0, 0, [[0, 100001], [2, 1]]))
