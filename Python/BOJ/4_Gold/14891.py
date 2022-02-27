# 톱니바퀴
import sys
input = sys.stdin.readline

gears = [0] + [list(map(int, input().rstrip())) for _ in range(4)]
N = int(input())
cmds = [list(map(int, input().split())) for _ in range(N)]

rotate_idx = [0, [2], [6, 2], [6, 2], [6]]

for target, direction in cmds:
    if target == 1:
        if gears[target][rotate_idx[target][0]] + gears[target+1][rotate_idx[target+1][0]] == 1:
            rotate_idx[target+1][0] += direction
            rotate_idx[target+1][0] %= 8
            if gears[target+1][rotate_idx[target+1][1]] + gears[target+2][rotate_idx[target+2][0]] == 1:
                rotate_idx[target+2][0] -= direction
                rotate_idx[target+2][0] %= 8
                if gears[target+2][rotate_idx[target+2][1]] + gears[target+3][rotate_idx[target+3][0]] == 1:
                    rotate_idx[target+3][0] += direction
                    rotate_idx[target+3][0] %= 8
                rotate_idx[target+2][1] -= direction
                rotate_idx[target+2][1] %= 8
            rotate_idx[target+1][1] += direction
            rotate_idx[target+1][1] %= 8
        rotate_idx[target][0] -= direction
        rotate_idx[target][0] %= 8

    elif target == 2:
        if gears[target][rotate_idx[target][1]] + gears[target+1][rotate_idx[target+1][0]] == 1:
            rotate_idx[target+1][0] += direction
            rotate_idx[target+1][0] %= 8
            if gears[target+1][rotate_idx[target+1][1]] + gears[target+2][rotate_idx[target+2][0]] == 1:
                rotate_idx[target+2][0] -= direction
                rotate_idx[target+2][0] %= 8
            rotate_idx[target+1][1] += direction
            rotate_idx[target+1][1] %= 8
        rotate_idx[target][1] -= direction
        rotate_idx[target][1] %= 8

        if gears[target][rotate_idx[target][0]] + gears[target-1][rotate_idx[target-1][0]] == 1:
            rotate_idx[target-1][0] += direction
            rotate_idx[target-1][0] %= 8
        rotate_idx[target][0] -= direction
        rotate_idx[target][0] %= 8

    elif target == 3:
        if gears[target][rotate_idx[target][1]] + gears[target+1][rotate_idx[target+1][0]] == 1:
            rotate_idx[target+1][0] += direction
            rotate_idx[target+1][0] %= 8
        rotate_idx[target][1] -= direction
        rotate_idx[target][1] %= 8

        if gears[target][rotate_idx[target][0]] + gears[target-1][rotate_idx[target-1][1]] == 1:
            rotate_idx[target-1][1] += direction
            rotate_idx[target-1][1] %= 8
            if gears[target-1][rotate_idx[target-1][0]] + gears[target-2][rotate_idx[target-2][0]] == 1:
                rotate_idx[target-2][0] -= direction
                rotate_idx[target-2][0] %= 8
            rotate_idx[target-1][0] += direction
            rotate_idx[target-1][0] %= 8
        rotate_idx[target][0] -= direction
        rotate_idx[target][0] %= 8

    else:
        if gears[target][rotate_idx[target][0]] + gears[target-1][rotate_idx[target-1][1]] == 1:
            rotate_idx[target-1][1] += direction
            rotate_idx[target-1][1] %= 8
            if gears[target-1][rotate_idx[target-1][0]] + gears[target-2][rotate_idx[target-2][1]] == 1:
                rotate_idx[target-2][1] -= direction
                rotate_idx[target-2][1] %= 8
                if gears[target-2][rotate_idx[target-2][0]] + gears[target-3][rotate_idx[target-3][0]] == 1:
                    rotate_idx[target-3][0] += direction
                    rotate_idx[target-3][0] %= 8
                rotate_idx[target-2][0] -= direction
                rotate_idx[target-2][0] %= 8
            rotate_idx[target-1][0] += direction
            rotate_idx[target-1][0] %= 8
        rotate_idx[target][0] -= direction
        rotate_idx[target][0] %= 8

result = 0
result += gears[1][(rotate_idx[1][0]-2)%8] * 2**0
for i in range(2,5):
    result += gears[i][(rotate_idx[i][0]+2)%8] * 2**(i-1)
print(result)
