# 주사위 굴리기 2

# 구른다! 막히면 반대로 구른다!
# 좌상단 (1, 1)
# 주사위 윗면 1, 바닥 6, 오른쪽 3
# 아랫면 숫자와 보드의 숫자를 비교해 방향 정함
# A > B 90도 시계방향
# A < B 90도 반시계방향
# A == B 방향 그대로
#   B
# L U R
#   F
#   D

drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 동남서북(시계방향)
dice = {
    'U': 1,
    'B': 2,
    'R': 3,
    'L': 4,
    'F': 5,
    'D': 6,
}
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
score_board = [[0]*M for _ in range(N)]
r, c = 0, 0
direction = 0

result = 0
for _ in range(K):
    dr, dc = drc[direction]
    r += dr
    c += dc
    if not (0 <= r < N and 0 <= c < M):   # 범위 벗어나면 반대방향으로
        r -= 2*dr
        c -= 2*dc
        direction = (direction+2) % 4

    if direction == 0:      # 동쪽
        dice['R'], dice['D'], dice['L'], dice['U'] = dice['U'], dice['R'], dice['D'], dice['L']

    elif direction == 1:    # 남쪽
        dice['F'], dice['D'], dice['B'], dice['U'] = dice['U'], dice['F'], dice['D'], dice['B']

    elif direction == 2:    # 서쪽
        dice['U'], dice['R'], dice['D'], dice['L'] = dice['R'], dice['D'], dice['L'], dice['U']

    else:                   # 북쪽
        dice['U'], dice['F'], dice['D'], dice['B'] = dice['F'], dice['D'], dice['B'], dice['U']

    A = dice['D']
    B = board[r][c]

    # 점수 계산
    if score_board[r][c]:    # 계산된 점수가 있는 경우
        result += score_board[r][c]*B

    else:
        stack = [(r, c)]
        score_board[r][c] = 1   # 점수보드로 방문체크
        idx = 0
        while idx < len(stack):
            _r, _c = stack[idx]
            for dr, dc in drc:
                nr = _r + dr
                nc = _c + dc
                if 0 <= nr < N and 0 <= nc < M and not score_board[nr][nc] and board[nr][nc] == B:
                    score_board[nr][nc] = 1
                    stack.append((nr, nc))
            idx += 1

        # 점수를 한번만 계산해주기 위해 점수보드에 저장
        score = len(stack)
        for _r, _c in stack:
            score_board[_r][_c] = score

        result += score*B

    # 방향전환
    if A > B:
        direction = (direction + 1) % 4
    elif A < B:
        direction = (direction - 1) % 4

print(result)
