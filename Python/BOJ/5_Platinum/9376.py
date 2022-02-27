# 탈옥
from collections import deque
import sys
input = sys.stdin.readline


def find_prisoner():
    prisoners = []
    for r in range(h):
        for c in range(w):
            if prison[r][c] == '$':
                prison[r][c] = '.'
                prisoners.append((r, c))
                if len(prisoners) > 1:
                    return prisoners


def escape(prisoners):
    board_ab = [[987654321]*w for _ in range(h)]
    board_a = [[987654321]*w for _ in range(h)]
    board_b = [[987654321]*w for _ in range(h)]

    que_ab = deque()
    que_a = deque([prisoners[0]])
    que_b = deque([prisoners[1]])

    r, c = prisoners[0]
    board_a[r][c] = 0
    visited[r][c] = 1
    r, c = prisoners[1]
    board_b[r][c] = 0
    visited[r][c] = 2

    min_ab = 987654321
    min_a = 987654321
    min_b = 987654321

    while que_a or que_b or que_ab:
        if que_ab:
            r, c = que_ab.popleft()
            visited[r][c] = 3
            for dr, dc in drc:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < h and 0 <= nc < w):
                    min_ab = min(min_ab, board_ab[r][c])
                    continue

                if prison[nr][nc] == '#' and board_ab[nr][nc] > board_ab[r][c] + 1:
                    que_ab.append((nr, nc))
                    board_ab[nr][nc] = board_ab[r][c] + 1

                elif prison[nr][nc] == '.' and board_ab[nr][nc] > board_ab[r][c]:
                    que_ab.append((nr, nc))
                    board_ab[nr][nc] = board_ab[r][c]

        if que_a:
            r, c = que_a.popleft()
            for dr, dc in drc:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < h and 0 <= nc < w):
                    min_a = min(min_a, board_a[r][c])
                    continue

                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1

                if prison[nr][nc] == '#' and board_a[nr][nc] > board_a[r][c] + 1:
                    que_a.append((nr, nc))
                    board_a[nr][nc] = board_a[r][c] + 1

                elif prison[nr][nc] == '.' and board_a[nr][nc] > board_a[r][c]:
                    que_a.append((nr, nc))
                    board_a[nr][nc] = board_a[r][c]

                if visited[nr][nc] == 2:
                    if prison[nr][nc] == '#':
                        que_ab.append((nr, nc))
                        visited[nr][nc] = 3
                        board_ab[nr][nc] = min(
                            board_ab[nr][nc], board_a[nr][nc] + board_b[nr][nc] - 1)
                    if prison[nr][nc] == '.':
                        visited[nr][nc] = 3
                        board_ab[nr][nc] = min(
                            board_ab[nr][nc], board_a[nr][nc] + board_b[nr][nc])

        if que_b:
            r, c = que_b.popleft()
            for dr, dc in drc:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < h and 0 <= nc < w):
                    min_b = min(min_b, board_b[r][c])
                    continue

                if visited[nr][nc] == 0:
                    visited[nr][nc] = 2

                if prison[nr][nc] == '#' and board_b[nr][nc] > board_b[r][c] + 1:
                    que_b.append((nr, nc))
                    board_b[nr][nc] = board_b[r][c] + 1

                elif prison[nr][nc] == '.' and board_b[nr][nc] > board_b[r][c]:
                    que_b.append((nr, nc))
                    board_b[nr][nc] = board_b[r][c]

                if visited[nr][nc] == 1:
                    if prison[nr][nc] == '#':
                        que_ab.append((nr, nc))
                        visited[nr][nc] = 3
                        board_ab[nr][nc] = min(
                            board_ab[nr][nc], board_a[nr][nc] + board_b[nr][nc] - 1)
                    if prison[nr][nc] == '.':
                        visited[nr][nc] = 3
                        board_ab[nr][nc] = min(
                            board_ab[nr][nc], board_a[nr][nc] + board_b[nr][nc])

    return min(min_ab, min_a + min_b)


T = int(input())
drc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
result = []
for tc in range(T):
    h, w = map(int, input().split())
    prison = [list(input()) for _ in range(h)]
    prisoners = find_prisoner()
    visited = [[0]*w for _ in range(h)]
    min_cnt = escape(prisoners)
    result.append(min_cnt)

print(*result, sep='\n')
