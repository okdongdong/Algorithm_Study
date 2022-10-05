def solution(strs, t):
    strs_set = set(strs)
    N = len(t)
    dp = [20001]*N

    for i in range(min(5, N)):
        dp[i] = 1 if t[:i+1] in strs_set else 20001

    for i in range(N):
        for j in range(5):
            if i-j < 1:
                continue

            if t[i-j:i+1] in strs_set:
                dp[i] = min(dp[i], dp[i-j-1] + 1)

    return dp[-1] if dp[-1] < 20001 else -1
