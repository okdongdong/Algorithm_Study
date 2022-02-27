# 배열에서 이동
from collections import deque
import sys
input = sys.stdin.readline


def bfs(min_val, max_val):

    que = deque([(0, 0)])
    visited = [[False]*N for _ in range(N)]
    visited[0][0] = True

    while que:
        r, c = que.popleft()
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if (nr, nc) == (N-1, N-1):
                return True

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = True
                if min_val <= arr[nr][nc] <= max_val:
                    que.append((nr, nc))

    return False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
min_diff = 201
min_val = min(arr[0][0], arr[-1][-1])
max_val = max(arr[0][0], arr[-1][-1])
nums = []

for r in range(N):
    nums += arr[r]

nums = sorted(list(set(nums)))


mn_idx = 0
for i in range(len(nums)-1, -1, -1):
    if nums[i] == max_val:
        mx_idx = i
        break

while mx_idx < len(nums) and nums[mn_idx] <= min_val:
    mn_val = nums[mn_idx]
    mx_val = nums[mx_idx]
    if bfs(mn_val, mx_val):
        min_diff = min(min_diff, mx_val - mn_val)
        mn_idx += 1

    else:
        mx_idx += 1

print(min_diff)
