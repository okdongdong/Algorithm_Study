# 상어 중학교

# 블록그룹: 2개이상의 블록으로 구성, 같은 색 + 무지개색
# 가장 큰 그룹을 제거, 크기 -> 무지개블럭 -> 기준블럭 행번호 큰 것 -> 열번호 큰 것
# 기준 블럭은 블럭중에서 좌상단에 있는 블럭

from copy import deepcopy


def rotate():
    temp_arr = deepcopy(arr)

    for r in range(N):
        for c in range(N):
            arr[r][c] = temp_arr[c][N-1-r]


def gravity():
    for c in range(N):
        temp_list = []
        stop = N
        flag = True
        for r in range(N):
            if arr[r][c] == 9:  # 빈칸일 경우
                flag = False
                continue
            if arr[r][c] == -1:
                stop = r
                _r = stop-1

                while temp_list:
                    arr[_r][c] = temp_list.pop()
                    _r -= 1
                while _r >= 0 and arr[_r][c] != -1:
                    arr[_r][c] = 9
                    _r -= 1
                stop = N
                continue

            temp_list.append(arr[r][c])

        if flag:
            continue

        r = stop-1
        while temp_list:
            arr[r][c] = temp_list.pop()
            r -= 1
        while r >= 0 and arr[r][c] != -1:
            arr[r][c] = 9
            r -= 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
drc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
result = 0

while True:
    visited = [[False]*N for _ in range(N)]
    max_group = []
    max_color = 9
    max_rainbow_cnt = 0
    max_r, max_c = 0, 0  # 최대 블록 기준점의 좌표
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue

            if arr[r][c] > 8 or arr[r][c] < 1:  # 삭제한 색이거나 검은색이거나 무지개색이면 continue
                continue

            now_color = arr[r][c]   # 현재 색 저장
            stack = set([(r, c)])
            now_r, now_c = r, c  # 현재블록 기준점의 좌표
            now_group = []
            now_rainbow_cnt = 0
            del_visited_list = []
            while stack:    # 블록 개수를 세어준다.
                _r, _c = stack.pop()
                now_group.append((_r, _c))

                if arr[_r][_c] == 0:    # 무지개 블럭 개수 카운트
                    now_rainbow_cnt += 1
                    del_visited_list.append((_r, _c))

                visited[_r][_c] = True

                for dr, dc in drc:
                    nr = _r+dr
                    nc = _c+dc
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        if arr[nr][nc] == now_color or arr[nr][nc] == 0:
                            stack.add((nr, nc))

            # 최대 블럭 구함
            max_group, max_rainbow_cnt, max_r, max_c, max_color = sorted([(max_group, max_rainbow_cnt, max_r, max_c, max_color),
                                                                          (now_group, now_rainbow_cnt, now_r, now_c, now_color)],
                                                                         key=lambda x: (len(x[0]), x[1], x[2], x[3]))[1]

            for _r, _c in del_visited_list:     # 무지개 블럭을 방문해제시켜줌
                visited[_r][_c] = False

    if len(max_group) <= 1:
        break

    for r, c in max_group:
        arr[r][c] = 9

    result += len(max_group)**2  # 점수추가
    gravity()   # 중력 -> 회전 -> 중력
    rotate()
    gravity()

print(result)
