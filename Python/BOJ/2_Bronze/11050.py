N, K = map(int, input().split())
K = max(K, N-K)

for i in range(N-K+1, N):
    N*=i

for i in range(1, K):
    K*=i

print(N//K)