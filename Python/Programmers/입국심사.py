def solution(n, times):
    left = 1
    right = int(1e18)

    while left < right:
        mid = (left + right) // 2

        now_n = sum(map(lambda time: mid // time, times))

        if now_n >= n:
            right = mid

        else:
            left = mid + 1

    return right
