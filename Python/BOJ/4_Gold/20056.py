# 마법사 상어와 파이어볼

N, M, K = map(int, input().split())
fireballs = [list(map(int, input().split())) for _ in range(M)]
drc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    field = {}
    mixball = set()
    temp_balls = []
    for r, c, m, s, d in fireballs:
        r = (r + drc[d][0]*s) % N
        c = (c + drc[d][1]*s) % N
        if not field.get((r, c)):
            field[(r, c)] = [(m, s, d)]
        else:
            mixball.add((r, c))
            field[(r, c)].append((m, s, d))

    for (r, c) in field.keys():
        # 파이어볼이 합쳐지는 경우
        if (r, c) in mixball:
            total_m = 0
            total_s = 0
            pre_d = field[(r, c)][0][2] % 2
            flag = 0
            for m, s, d in field[(r, c)]:
                total_m += m
                total_s += s
                if pre_d != d % 2:
                    flag = 1
            total_m //= 5
            if not total_m:
                continue
            total_s //= len(field[(r, c)])
            for next_d in range(flag, 8, 2):
                temp_balls.append((r, c, total_m, total_s, next_d))

        else:
            m, s, d = field[(r, c)][0]
            temp_balls.append((r, c, m, s, d))

    fireballs = temp_balls

result = 0
for r, c, m, s, d in fireballs:
    result += m

print(result)
