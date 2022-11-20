from heapq import heapify, heappop, heappush
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arr = [[0] * M for _ in range(N)]
arr[0][0] = 1

# 최대힙으로 사용하기 위해 높이를 음수로 저장
que = [(-board[0][0], 0, 0)]

while que:
    height, r, c = heappop(que)
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        # 갈수 있는 지점인지 확인
        if not (0 <= nr < N and 0 <= nc < M) or board[nr][nc] >= board[r][c]:
            continue

        # 아마 방문한 지점인지 확인
        # 방문한 적 없는 지점만 다음에 이동할 지점으로 추가해줌
        if not arr[nr][nc]:
            heappush(que, (-board[nr][nc], nr, nc))

        # 경우의 수 추가
        arr[nr][nc] += arr[r][c]

print(arr[-1][-1])
