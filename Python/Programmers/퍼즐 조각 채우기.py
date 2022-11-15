from collections import defaultdict


def solution(game_board, table):
    N = len(game_board)
    drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def rotation(board):
        new_board = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                new_board[r][c] = board[N - 1 - c][r]

        return new_board

    def find_space(board):
        blocks = []
        visited = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if board[r][c] == 0 and not visited[r][c]:
                    block = []
                    stack = [(r, c)]
                    while stack:
                        _r, _c = stack.pop()
                        if visited[_r][_c]:
                            continue
                        visited[_r][_c] = True
                        block.append((_r - r, _c - c))
                        for dr, dc in drc:
                            nr, nc = _r + dr, _c + dc
                            if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
                                continue

                            if board[nr][nc] == 0:
                                stack.append((nr, nc))

                    blocks.append(tuple(sorted(block)))
        return blocks

    def find_block(board):
        blocks = []
        visited = [[False] * N for _ in range(N)]
        block_num = 2
        for r in range(N):
            for c in range(N):
                if board[r][c] and not visited[r][c]:
                    block = []
                    stack = [(r, c)]
                    while stack:
                        _r, _c = stack.pop()
                        if visited[_r][_c]:
                            continue
                        visited[_r][_c] = True
                        if board[_r][_c] < 2:
                            board[_r][_c] = block_num
                        block.append((_r - r, _c - c))
                        for dr, dc in drc:
                            nr, nc = _r + dr, _c + dc
                            if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
                                continue

                            if board[nr][nc]:
                                stack.append((nr, nc))

                    puzzles[board[r][c]].add(tuple(sorted(block)))
                    block_num += 1

        return blocks

    spaces = find_space(game_board)
    puzzles = defaultdict(set)

    find_block(table)
    table = rotation(table)
    find_block(table)
    table = rotation(table)
    find_block(table)
    table = rotation(table)
    find_block(table)

    visited = set()

    for space in spaces:
        for key, val in puzzles.items():
            if key in visited:
                continue

            if space in val:
                visited.add(key)
                break

    return sum(map(lambda x: len(puzzles[x].pop()), visited))


print(
    solution(
        [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1],
        ],
        [
            [1, 0, 0, 0, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0],
        ],
    )
)
