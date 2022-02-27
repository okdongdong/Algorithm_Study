# 토너먼트
N, A, B = map(int, input().split())
result = 0
while A != B:
    result += 1
    A = (A+1)>>1
    B = (B+1)>>1
print(result)
