import sys

input = sys.stdin.readline
N, M = map(int, input().split())

matrix1 = [list(map(int, list(input().rstrip()))) for _ in range(N)]
matrix2 = [list(map(int, list(input().rstrip()))) for _ in range(N)]


def reverse(r, c):
    for i in range(3):
        for j in range(3):
            matrix1[r+i][c+j] = 1-matrix1[r+i][c+j]


def solution():
    cnt = 0
    for r in range(N):
        for c in range(M):
            if matrix1[r][c] == matrix2[r][c]:
                continue

            if r > N-3 or c > M-3:
                return -1

            reverse(r, c)
            cnt += 1

    return cnt


print(solution())
