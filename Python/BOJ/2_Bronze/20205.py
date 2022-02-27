# 교수님 그림이 깨지는데요?
N, K = map(int, input().split())
arr = [input().split() for _ in range(N)]
for i in range(N):
    temp = []
    for j in range(N):
        temp += [arr[i][j]]*K

    for k in range(K):
        print(' '.join(temp))
