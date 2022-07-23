def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 102
    rect_arr = [[0]*N for _ in range(N)]
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dxy2 = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

    # 사각형을 배열에 표시
    for sx, sy, ex, ey in rectangle:

        for x in range(2*sx, 2*ex+1):
            for y in range(2*sy, 2*ey+1):
                rect_arr[x][y] = 1

    # 테두리만 남기고 내부 제거
    for x in range(N):
        for y in range(N):
            if not rect_arr[x][y]:
                continue

            for dx, dy in dxy+dxy2:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                if not rect_arr[nx][ny]:
                    break

            else:
                rect_arr[x][y] = 2

    que = [(2*characterX, 2*characterY)]
    rect_arr[2*characterX][2*characterY] = 0
    result = 0

    while que:
        temp = []
        for x, y in que:
            if (x, y) == (2*itemX, 2*itemY):
                return result//2

            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                if rect_arr[nx][ny] == 1:
                    temp.append((nx, ny))
                    rect_arr[nx][ny] = 0

        result += 1
        que = temp


print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [
      4, 3, 6, 9], [2, 6, 8, 8]]	, 1	, 3	, 7	, 8	))
print(solution([[1, 1, 8, 4], [2, 2, 4, 9], [
      3, 6, 9, 8], [6, 3, 7, 7]]	, 9	, 7	, 6	, 1	))
print(solution([[1, 1, 5, 7]]	, 1	, 1	, 4	, 7	))
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]]	, 3	, 1	, 7	, 10	))
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]]	, 1	, 4	, 6	, 3	))
print(solution([[1, 1, 3, 7], [2, 2, 7, 4], [4, 3, 6, 6]], 1, 2, 6, 6))
