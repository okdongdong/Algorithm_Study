# 행렬 덧셈
N, M = map(int, input().split())
arr = [[0]*M for _ in range(N)]

for _ in range(2):
    for r in range(N):
        nums = list(map(int, input().split()))
        for c in range(M):
            arr[r][c] += nums[c]

for r in range(N):
    print(*arr[r])
