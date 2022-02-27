# ⚾

import sys
input = sys.stdin.readline


def swap(depth, i):
    nums[depth], nums[i] = nums[i], nums[depth]


def cal_score():
    global max_score
    idx = 0  # 현재 순서 인덱스
    score = 0
    order = nums[:3] + [0] + nums[3:]
    for inning in range(N):
        out_cnt = 0
        field = []

        while out_cnt < 3:
            hit_ball = inning_list[inning][order[idx]]

            if hit_ball == 0:
                out_cnt += 1

            else:
                field.append(hit_ball)

            idx += 1
            if idx == 9:
                idx = 0

        else:
            score += len(field)
            temp = 0
            for i in range(len(field)-1, -1, -1):
                temp += field[i]
                if temp >= 4:
                    break
                score -= 1

    if max_score < score:
        max_score = score


def perm(depth):
    if depth == 7:
        cal_score()
        return

    for i in range(depth, 8):
        swap(depth, i)
        perm(depth+1)
        swap(depth, i)


N = int(input())
inning_list = [list(map(int, input().split())) for _ in range(N)]
player_order_list = []
max_score = 0
nums = [1, 2, 3, 4, 5, 6, 7, 8]
perm(0)
print(max_score)
