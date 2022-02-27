# 모노미노도미노 2
import sys
input = sys.stdin.readline


def move(block_num, c):  # green을 기준으로
    global arr

    if block_num == 1:
        for r in range(5):
            if r < 4 and not arr[r][c]:
                continue
            if r > 0:
                arr[r-1][c] = 1
            else:   # 블록이 칸을 벗어났을 때
                arr.pop()
                temp = [0]*4
                temp[c] = 1
                arr = [temp] + arr
            break
        boom()

    elif block_num == 2:
        for r in range(5):
            if r < 4 and not (arr[r][c] or arr[r][c+1]):
                continue
            if r > 0:
                arr[r-1][c] = 1
                arr[r-1][c+1] = 1
            else:
                arr.pop()
                temp = [0]*4
                temp[c] = 1
                temp[c+1] = 1
                arr = [temp] + arr
            break
        boom()

    else:
        for _ in range(2):
            for r in range(5):
                if r < 4 and not arr[r][c]:
                    continue
                if r > 0:
                    arr[r-1][c] = 1
                else:
                    arr.pop()
                    temp = [0]*4
                    temp[c] = 1
                    arr = [temp] + arr
                break
            boom()


def boom():
    global arr, score
    cnt = 0
    for r in range(3, -1, -1):
        for c in range(4):
            if not arr[r][c]:
                break
        else:
            arr.pop(r)
            cnt += 1
    score += cnt
    arr = [[0]*4 for _ in range(cnt)] + arr


N = int(input())
t_x_y_list = [list(map(int, input().split())) for _ in range(N)]

score = 0

# 초록색 영역
arr = [[0]*4 for _ in range(4)]
for t, x, y in t_x_y_list:
    move(t, y)
green_sum = sum(map(sum, arr))

# 파란색 영역
arr = [[0]*4 for _ in range(4)]
for t, x, y in t_x_y_list:
    if t != 1:
        t = 5-t
    move(t, x)
blue_sum = sum(map(sum, arr))

print(score)
print(green_sum + blue_sum)
