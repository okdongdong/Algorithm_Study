# 마법사 상어와 파이어스톰

# 1. 남아있는 얼음의 합
# 2. 가장 큰 덩어리가 차지하는 칸의 개수

def rotate(_size, s_r, s_c):
    temp_arr = [[0]*_size for _ in range(_size)]
    # 배열 복사
    for _r in range(_size):
        for _c in range(_size):
            temp_arr[_r][_c] = arr[_r+s_r][_c+s_c]

    # 돌려서 붙이기
    for _r in range(_size):
        for _c in range(_size):
            arr[_r+s_r][_c+s_c] = temp_arr[_size-1-_c][_r]


def ice_size(_size):
    global max_ice_size
    visited = [[False]*_size for _ in range(_size)]
    for _r in range(_size):
        for _c in range(_size):
            if visited[_r][_c] or not arr[_r][_c]:
                continue
            stack = [(_r, _c)]
            visited[_r][_c] = True
            idx = 0
            while idx < len(stack):
                __r, __c = stack[idx]
                for dr, dc in drc:
                    nr = __r + dr
                    nc = __c + dc
                    if 0 <= nr < _size and 0 <= nc < _size and not visited[nr][nc] and arr[nr][nc]:
                        visited[nr][nc] = True
                        stack.append((nr, nc))

                idx += 1    # idx == 현재 얼음의 크기

            # 가장 큰 얼음덩어리의 크기를 구함
            if max_ice_size < idx:
                max_ice_size = idx


N, Q = map(int, input().split())
arr_size = 2**N     # 2**N짜리 배열
arr = [list(map(int, input().split())) for _ in range(arr_size)]
L_list = list(map(int, input().split()))
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for L in L_list:
    size = 2**L
    if size != arr_size:
        for r in range(0, arr_size, size):
            for c in range(0, arr_size, size):
                rotate(size, r, c)

    # 얼음녹이기
    melt_list = []
    for r in range(arr_size):
        for c in range(arr_size):
            if not arr[r][c]:
                continue

            cnt = 0
            for dr, dc in drc:
                nr = r+dr
                nc = c+dc
                if 0 <= nr < arr_size and 0 <= nc < arr_size and arr[nr][nc]:
                    cnt += 1
                    if cnt > 2:
                        break
            else:
                melt_list.append((r, c))

    for r, c in melt_list:
        arr[r][c] -= 1

max_ice_size = 0
ice_size(arr_size)
print(sum(map(sum, arr)))
print(max_ice_size)
