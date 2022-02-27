N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
A = sorted(A)
B = sorted(B, reverse=True)
result = 0

for i in range(N):
    result += A[i]*B[i]

print(result)