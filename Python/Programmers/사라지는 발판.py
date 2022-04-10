def solution(board, aloc, bloc):
    drc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    a_win_cnt = [987654321, 0]
    b_win_cnt = [0, 987654321]

    R, C = len(board), len(board[0])

    def move_a(ar, ac, br, bc, acnt, bcnt):
        nonlocal a_win_cnt, b_win_cnt

        # b가 움직여서 같은위치가 되는 경우
        if (ar, ac) == (br, bc):
            # 움직일수 있어야 함
            for dr, dc in drc:
                nr, nc = ar + dr, ac+dc
                if not(0 <= nr < R and 0 <= nc < C) or not board[nr][nc]:
                    continue
                # 움직일 수 있다면 => a승
                # b_win_cnt = min(b_win_cnt, acnt + 1)
                if a_win_cnt[0] > acnt:
                    a_win_cnt[0] = acnt + 1
                    a_win_cnt[1] = bcnt
                elif a_win_cnt[0] == acnt:
                    a_win_cnt[1] = max(a_win_cnt[1], bcnt)

                if b_win_cnt[1] < bcnt:
                    b_win_cnt[1] = bcnt
                    b_win_cnt[0] = acnt + 1
                elif b_win_cnt[1] == bcnt:
                    b_win_cnt[0] = min(b_win_cnt[0], acnt)
                break
            else:
                # 움직일 수 없다면 => b승
                # b_win_cnt = min(b_win_cnt, bcnt)
                if a_win_cnt[0] < acnt:
                    a_win_cnt[0] = acnt
                    a_win_cnt[1] = bcnt
                elif a_win_cnt[0] == acnt:
                    a_win_cnt[1] = min(a_win_cnt[1], bcnt)

                if b_win_cnt[1] > bcnt:
                    b_win_cnt[1] = bcnt
                    b_win_cnt[0] = acnt
                elif b_win_cnt[1] == bcnt:
                    b_win_cnt[0] = max(b_win_cnt[0], acnt)

            return

        flag = True
        for dr, dc in drc:
            nr, nc = ar + dr, ac+dc
            if not(0 <= nr < R and 0 <= nc < C) or not board[nr][nc]:
                continue

            board[ar][ac] = 0
            move_b(nr, nc, br, bc, acnt+1, bcnt)
            board[ar][ac] = 1

            flag = False
        # 움직일수 없으므로 a의 패배, b승
        if flag:
            if a_win_cnt[0] < acnt:
                a_win_cnt[0] = acnt
                a_win_cnt[1] = bcnt
            elif a_win_cnt[0] == acnt:
                a_win_cnt[1] = min(a_win_cnt[1], bcnt)

            if b_win_cnt[1] > bcnt:
                b_win_cnt[1] = bcnt
                b_win_cnt[0] = acnt
            elif b_win_cnt[1] == bcnt:
                b_win_cnt[0] = max(b_win_cnt[0], acnt)
            # a_win_cnt = max(a_win_cnt, acnt)

    def move_b(ar, ac, br, bc, acnt, bcnt):
        nonlocal a_win_cnt, b_win_cnt

        # a가 움직여서 같은위치가 되었으므로 b승
        if (ar, ac) == (br, bc):
            for dr, dc in drc:
                nr, nc = br + dr, bc+dc
                if not(0 <= nr < R and 0 <= nc < C) or not board[nr][nc]:
                    continue
                # b_win_cnt = min(b_win_cnt, bcnt+1)
                if a_win_cnt[1] > bcnt:
                    a_win_cnt[1] = bcnt+1
                    a_win_cnt[0] = acnt
                elif a_win_cnt[1] == bcnt:
                    a_win_cnt[0] = max(a_win_cnt[0], acnt)

                if b_win_cnt[0] < acnt:
                    b_win_cnt[0] = acnt
                    b_win_cnt[1] = bcnt+1
                elif b_win_cnt[0] == bcnt:
                    b_win_cnt[1] = min(b_win_cnt[1], bcnt)
                break
            else:
                if a_win_cnt[1] < bcnt:
                    a_win_cnt[1] = bcnt
                    a_win_cnt[0] = acnt
                elif a_win_cnt[1] == bcnt:
                    a_win_cnt[0] = min(a_win_cnt[0], acnt)

                if b_win_cnt[0] > acnt:
                    b_win_cnt[0] = acnt
                    b_win_cnt[1] = bcnt
                elif b_win_cnt[0] == acnt:
                    b_win_cnt[1] = max(b_win_cnt[1], bcnt)
                # b_win_cnt = min(b_win_cnt, acnt)
            return

        flag = True
        for dr, dc in drc:
            nr, nc = br + dr, bc+dc
            if not(0 <= nr < R and 0 <= nc < C) or not board[nr][nc]:
                continue

            board[br][bc] = 0
            move_a(ar, ac, nr, nc, acnt, bcnt+1)
            board[br][bc] = 1

            flag = False

        if flag:    # 움직일수가 없으므로 b의 패배, a승
            # a_win_cnt = max(a_win_cnt, bcnt)
            if a_win_cnt[1] < bcnt:
                a_win_cnt[1] = bcnt
                a_win_cnt[0] = acnt
            elif a_win_cnt[1] == bcnt:
                a_win_cnt[0] = min(a_win_cnt[0], acnt)

            if b_win_cnt[0] > acnt:
                b_win_cnt[0] = acnt
                b_win_cnt[1] = bcnt
            elif b_win_cnt[0] == acnt:
                b_win_cnt[1] = max(b_win_cnt[1], bcnt)
            return

    move_a(*aloc, *bloc, 0, 0)

    return min(sum(a_win_cnt), sum(b_win_cnt))


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],	[1, 0],	[1, 2]))
