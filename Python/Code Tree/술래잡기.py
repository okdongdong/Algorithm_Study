def runner_move(tr, tc):
    # 도망자 시작 : 가로-오른쪽 / 세로-아래쪽
    move_runners = find_runner(tr, tc)

    for r, c, d in move_runners:
        dr, dc = drc[d]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < N and 0 <= nc < N):
            d = (d + 2) % 4
            dr, dc = drc[d]
            nr, nc = r + dr, c + dc

        if (nr, nc) == (tr, tc):
            runners[r][c].append(d)

        else:
            runners[nr][nc].append(d)


def catch_runner(tr, tc, d):
    cnt = 0
    dr, dc = drc[d]
    for i in range(3):
        r, c = tr + dr * i, tc + dc * i

        if not (0 <= r < N and 0 <= c < N) or trees[r][c]:
            continue

        cnt += len(runners[r][c])
        runners[r][c] = []

    return cnt


def find_runner(tr, tc):
    move_runners = []
    for dr, dc in runner_move_area:
        r, c = tr + dr, tc + dc
        if not (0 <= r < N and 0 <= c < N):
            continue

        for d in runners[r][c]:
            move_runners.append((r, c, d))

        runners[r][c] = []

    return move_runners


def get_tagger_directions():
    tagger_dirs = []
    d = 3  # 상우하좌
    cnt = 1
    while True:
        for _ in range(2):
            for _ in range(cnt):
                tagger_dirs.append(d)

            d = (d + 1) % 4

            if cnt == N:
                tagger_dirs.pop()
                tagger_dirs += list(map(lambda x: (x + 2) % 4, tagger_dirs[::-1]))

                return tagger_dirs

        cnt += 1


N, M, H, K = map(int, input().split())
runners = [[[] for _ in range(N)] for _ in range(N)]
trees = [[False] * N for _ in range(N)]

# 도망자의 방향을 고려하여 작성
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 도망자
for _ in range(M):
    r, c, d = map(lambda x: int(x) - 1, input().split())
    runners[r][c].append(d)

# 나무
for _ in range(H):
    r, c = map(lambda x: int(x) - 1, input().split())
    trees[r][c] = True

# 도망자가 도망가는 영역
runner_move_area = {(0, 0)}
for _ in range(3):
    que = []
    for r, c in runner_move_area:
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            que.append((nr, nc))
    runner_move_area.update(que)

# 술래가 움직이는 방향 기록
tr, tc = N // 2, N // 2
tagger_dirs = get_tagger_directions()

score = 0

for turn in range(1, K + 1):
    runner_move(tr, tc)

    # 술래 움직임
    idx = (turn - 1) % len(tagger_dirs)
    d = tagger_dirs[idx]
    dr, dc = drc[d]

    tr, tc = tr + dr, tc + dc

    # 술래가 움직인 후 바라보는 방향
    idx = turn % len(tagger_dirs)
    nd = tagger_dirs[idx]

    score += turn * catch_runner(tr, tc, nd)

print(score)
