import sys

input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(lambda x: int(x) % 1000, input().split())) for _ in range(N)]


def mult_matrix(arr1, arr2):
    new_arr = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_arr[r][c] = cal(arr1, arr2, r, c)

    return new_arr


def cal(arr1, arr2, r, c):
    val = 0

    for i in range(N):
        val += arr1[r][i] * arr2[i][c]

    return val % 1000


def recur(b):
    if b == 1:
        return A

    if b % 2:
        arr = recur(b - 1)
        return mult_matrix(arr, A)

    arr = recur(b // 2)
    return mult_matrix(arr, arr)


result = recur(B)
for r in range(N):
    print(*result[r])
