def solution(money):
    N = len(money)
    dp1 = [0]*N  # 첫 집을 안 턴 경우
    dp2 = [0]*N  # 첫 집을 턴 경우

    dp1[1] = money[1]
    dp2[0] = money[0]

    for i in range(2, N):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])

    for i in range(1, N-1):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])

    return max(dp1[N-1], dp2[N-2], dp2[N-3])


print(solution([3, 2, 2]))
print(solution([10, 2, 2, 100, 2]))
