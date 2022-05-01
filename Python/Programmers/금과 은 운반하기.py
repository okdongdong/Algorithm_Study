def solution(a, b, g, s, w, t):

    left, right = 0, 10**15
    result = right
    while left <= right:
        mid = (left + right)//2
        gold, silver, total = 0, 0, 0

        for i in range(len(t)):
            # 현재시간 내에 갖다놓을 수 있는 횟수 계산
            cnt = (mid // (t[i]*2))
            cnt += 1 if mid % (t[i]*2) >= t[i] else 0

            # 옮길 수 있는 광물의 총량
            gold += min(g[i], cnt*w[i])
            silver += min(s[i], cnt*w[i])
            total += min(g[i] + s[i], cnt*w[i])

        # 기준을 충족하는지 확인
        if gold >= a and silver >= b and total >= a+b:
            right = mid - 1
            result = min(mid, result)

        else:
            left = mid + 1

    return result


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
