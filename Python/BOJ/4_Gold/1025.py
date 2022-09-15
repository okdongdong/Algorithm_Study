N, M = map(int, input().split())

nums = [list(input()) for _ in range(N)]
square_num_list = set([-1])


def square_check(num):
    if num == int(num**0.5)**2:
        square_num_list.add(num)


def create_num(sr, sc, dr, dc):
    num = ''
    r, c = sr, sc
    while 0 <= r < N and 0 <= c < M:
        num += nums[r][c]
        square_check(int(num))
        r += dr
        c += dc


for sr in range(N):
    for sc in range(M):
        for dr in range(-N, N):
            for dc in range(-M, M):
                if dr == 0 and dc == 0:
                    continue

                create_num(sr, sc, dr, dc)

print(max(square_num_list))
