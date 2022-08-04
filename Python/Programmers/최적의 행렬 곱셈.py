def solution(matrix_sizes):

    n = len(matrix_sizes)

    dp = [[987654321]*n for _ in range(n)]
    # distance == 0
    for i in range(n):
        dp[i][i] = 0

    # distance == 1
    for left in range(n-1):
        right = left + 1
        a, b = matrix_sizes[left]
        c = matrix_sizes[right][1]
        dp[left][right] = a*b*c

    for distance in range(2, n):
        for left in range(n-distance):
            right = left + distance
            a = matrix_sizes[left][0]
            c = matrix_sizes[right][1]
            for middle in range(left, right):

                b = matrix_sizes[middle][1]

                dp[left][right] = min(
                    dp[left][right], dp[left][middle] + dp[middle+1][right] + a*b*c)

    return dp[0][-1]


print(solution([[5, 3], [3, 10], [10, 6]]))  # 270
