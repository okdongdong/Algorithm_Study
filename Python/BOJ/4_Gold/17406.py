from copy import deepcopy
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cmds = [list(map(int, input().split())) for _ in range(K)]
min_val = float("inf")
visited = [False] * K


def recur(arr, cnt):
    global min_val
    if cnt == K:
        val = min(map(sum, arr))
        min_val = min(min_val, val)
        return

    for i in range(K):
        if visited[i]:
            continue

        visited[i] = True

        n_arr = deepcopy(arr)
        rotate(n_arr, cmds[i])
        recur(n_arr, cnt + 1)

        visited[i] = False


def rotate(arr, cmd):
    r, c, s = cmd
    r -= 1
    c -= 1

    for i in range(1, s + 1):
        sr, sc = r - i, c - i
        er, ec = r + i, c + i

        temp = []

        for _c in range(sc, ec):
            temp.append(arr[sr][_c])
        for _r in range(sr, er):
            temp.append(arr[_r][ec])
        for _c in range(ec, sc, -1):
            temp.append(arr[er][_c])
        for _r in range(er, sr, -1):
            temp.append(arr[_r][sc])

        idx = -1

        for _c in range(sc, ec):
            arr[sr][_c] = temp[idx]
            idx += 1
        for _r in range(sr, er):
            arr[_r][ec] = temp[idx]
            idx += 1
        for _c in range(ec, sc, -1):
            arr[er][_c] = temp[idx]
            idx += 1
        for _r in range(er, sr, -1):
            arr[_r][sc] = temp[idx]
            idx += 1


recur(arr, 0)
print(min_val)
