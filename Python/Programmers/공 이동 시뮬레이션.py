def solution(n, m, x, y, queries):
    def cal_area():
        nonlocal sr, sc, er, ec

        if is_row:
            if dx > 0 and sr == 0:
                er = min(max(er, sr+dx), n-1)

            elif dx < 0 and er == n-1:
                sr = max(min(sr, er+dx), 0)

            else:
                sr = max(0, sr+dx)
                er = min(n-1, er+dx)

        else:
            if dx > 0 and sc == 0:
                ec = min(max(ec, sc+dx), m-1)

            elif dx < 0 and ec == m-1:
                sc = max(min(sc, ec+dx), 0)

            else:
                sc = max(0, sc+dx)
                ec = min(m-1, ec+dx)

    is_row = queries[0][0] > 1
    dx = 0

    sr, sc = er, ec = x, y  # 좌상단, 우하단

    for i in range(len(queries)-1, -1, -1):
        command, temp_dx = queries[i]

        if is_row == (command > 1):
            # 쿼리압축
            dx += temp_dx * (-1)**(command % 2)
            continue

        cal_area()

        is_row = command > 1
        dx = temp_dx * (-1)**(command % 2)

    else:
        cal_area()

    cnt = (er-sr+1) * (ec-sc+1)

    return cnt


print(solution(2, 3, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
