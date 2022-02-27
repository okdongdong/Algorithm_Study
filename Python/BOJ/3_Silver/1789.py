# 수들의 합
S = int(input())
N = int((2*S-1)**.5)
print(N if N**2 + N <= 2*S else N-1)
