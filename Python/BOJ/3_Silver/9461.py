# 파도반 수열
memo = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
for i in range(11, 101):
    memo[i] = memo[i-1] + memo[i-5]
memo = list(map(str, memo))
result = []
N = int(input())
for _ in range(N):
    num = int(input())
    result.append(memo[num])
print('\n'.join(result))
