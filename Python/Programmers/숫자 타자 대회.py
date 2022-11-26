def solution(numbers):
    # 숫자로만 구성되어있음 -> 10개
    N = 10
    weights = [[0] * N for _ in range(N)]

    # 0대신 11을 넣어 위치 표시
    for num in list(range(1, 10)) + [11]:
        r1, c1 = divmod(num - 1, 3)
        num %= 11
        for target in list(range(num, 10)) + [11]:
            r2, c2 = divmod(target - 1, 3)
            target %= 11

            if r1 == r2 and c1 == c2:
                weights[num][target] = 1

            else:
                dr, dc = abs(r1 - r2), abs(c1 - c2)
                d = min(dr, dc) if dr and dc else 0  # 대각선이동횟수 계산
                drc = dr + dc - 2 * d  # 가로세로 이동횟수 계산

                weights[num][target] = d * 3 + drc * 2
                weights[target][num] = d * 3 + drc * 2

    INF = float("inf")
    dp = [[INF] * N for _ in range(N)]
    dp[4][6] = 0

    for number in numbers:
        number = int(number)
        # 손가락을 움직일 때마다 dp배열 생성
        temp_dp = [[INF] * N for _ in range(N)]
        for left in range(N):
            for right in range(N):
                if dp[left][right] == INF or left == right:  # 양손 중복 고려
                    continue

                temp_dp[left][number] = min(temp_dp[left][number], dp[left][right] + weights[right][number])
                temp_dp[number][right] = min(temp_dp[number][right], dp[left][right] + weights[left][number])

        dp = temp_dp

    return min(map(min, dp))


print(solution("1756"))
print(solution("5123"))
