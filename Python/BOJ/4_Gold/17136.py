# 색종이 붙이기

def search(r, c, n):
    for dr in range(n):
        for dc in range(n):
            if not (r+dr < N and c+dc < N) or not arr[r+dr][c+dc]:
                return False

    return True


def is_overlap():
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                return True
    return False


def cover_arr(r, c, n, cover=True):
    if cover:
        for dr in range(n):
            for dc in range(n):
                arr[r+dr][c+dc] -= 1
    else:
        for dr in range(n):
            for dc in range(n):
                arr[r+dr][c+dc] += 1


def check_arr(r, c):
    global min_cnt
    if sum(cnt_list) > min_cnt:
        return

    if r == N:
        r = 0
        c += 1
        if c == N:
            if not is_overlap():
                min_cnt = min(min_cnt, sum(cnt_list))
            return

    if arr[r][c] > 0:
        for size in range(size_arr[r][c], 0, -1):
            cover_arr(r, c, size)
            if cnt_list[size] < 5:
                cnt_list[size] += 1
                check_arr(r+1, c)
                cnt_list[size] -= 1
            cover_arr(r, c, size, False)

    elif arr[r][c] < 0:
        return

    else:
        check_arr(r+1, c)


# 10*10 범위
N = 10
arr = [list(map(int, input().split())) for _ in range(N)]
size_arr = [[0]*N for _ in range(N)]
min_cnt = 9999

for r in range(N):
    for c in range(N):
        if arr[r][c]:
            for i in range(1, 6):
                if not search(r, c, i):
                    break
                size_arr[r][c] = i

cnt_list = [0]*6
check_arr(0, 0)

if min_cnt == 9999:
    min_cnt = -1

print(min_cnt)
