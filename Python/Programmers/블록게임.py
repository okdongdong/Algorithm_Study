def solution(board):
    def drop_black_block():
        for c in range(N):
            for r in range(N):
                if board[r][c]:
                    if r >= 1:
                        board[r - 1][c] = -1
                    if r >= 2:
                        board[r - 2][c] = -1
                    break

    def rect_check(r, c, is_vertical):
        block_num = 0
        block_cnt = 0
        for dr in range(2 + is_vertical):
            for dc in range(3 - is_vertical):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 0:
                    return False

                if board[nr][nc] == -1:
                    continue

                if block_num and board[nr][nc] != block_num:
                    return False

                if not block_num and board[nr][nc]:
                    block_num = board[nr][nc]

                block_cnt += 1

        return block_cnt == 4

    N = len(board)
    answer = 0
    flag = True
    while flag:
        flag = False
        drop_black_block()

        for r in range(N):
            for c in range(N):
                if board[r][c] == 0:
                    continue

                for is_vertical in [True, False]:
                    if rect_check(r, c, is_vertical):
                        for dr in range(2 + is_vertical):
                            for dc in range(3 - is_vertical):
                                nr, nc = r + dr, c + dc
                                board[nr][nc] = 0
                        answer += 1
                        flag = True
                        break

                else:
                    if board[r][c] == -1:
                        board[r][c] = 0

    return answer


print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
            [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
            [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 5],
        ]
    )
)
