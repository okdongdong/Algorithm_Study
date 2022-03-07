def rotate(arr):
    N = len(arr)
    new_arr = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                new_arr[N-1-c][r] = 1

    return new_arr


def solution(key, lock):
    N = len(lock)
    M = len(key)
    lock_cnt = N**2 - sum(map(sum, lock))   # 홈의 개수
    key_cnt = sum(map(sum, key))            # 돌기의 개수

    if lock_cnt > key_cnt:  # 모든 key를 넣어도 다 채울수 없는 경우
        return False
    for _ in range(4):

        for i in range(-M, N):
            for j in range(-M, N):
                flag = False
                temp_cnt = 0

                for r in range(M):
                    if not(0 <= r+i < N):  # 범위를 벗어나는 경우
                        continue

                    for c in range(M):
                        if not(0 <= c+j < N):  # 범위를 벗어나는 경우
                            continue

                        if lock[r+i][c+j] + key[r][c] != 1:
                            flag = True
                            temp_cnt = 0
                            break

                        if key[r][c]:   # 키가 홈을 채우는 경우에만 카운트 증가
                            temp_cnt += 1

                        if temp_cnt == lock_cnt:    # 키가 모든 홈을 채웠을 때 true 리턴
                            return True

                    if flag:
                        break

        key = rotate(key)

    return False


print(solution([[0, 0, 0], [0, 0, 0], [1, 1, 0]],
      [[1, 1, 1], [1, 1, 0], [1, 1, 0]]))
print(solution([[0, 0, 0], [0, 0, 0], [1, 0, 0]],
      [[1, 1, 1], [1, 1, 1], [1, 1, 0]]))
