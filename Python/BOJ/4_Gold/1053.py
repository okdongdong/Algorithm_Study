def check(left, right):
    global min_cnt

    if left >= right:
        return 0

    if dp[left][right] < 0:
        dp[left][right] = min(check(left + 1, right - 1) + (txt[left] != txt[right]), check(left + 1, right) + 1, check(left, right - 1) + 1)

    return dp[left][right]


txt = list(input())
N = len(txt)
left, right = 0, N - 1

dp = [[-1] * N for _ in range(N)]
min_cnt = check(left, right)

for i in range(N - 1):
    for j in range(i + 1, N):
        dp = [[-1] * N for _ in range(N)]
        txt[i], txt[j] = txt[j], txt[i]
        min_cnt = min(min_cnt, check(left, right) + 1)
        txt[i], txt[j] = txt[j], txt[i]

print(min_cnt)
