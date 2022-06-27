def solution(a):
    N = len(a)
    if N < 2:
        return 0
    result = 0

    num_dict = {}
    num_set = set(a)
    # dict key 추가
    for num in num_set:
        num_dict[num] = 0

    # dict cnt 계산
    for num in a:
        num_dict[num] += 1

    # num 별 최대 길이 계산
    for num in num_set:
        # 길이의 최대크기제한
        result_limit = num_dict[num]*2
        if result_limit <= result:
            continue

        # 실제길이 계산
        stack = []
        temp_cnt = 0
        for num1 in a:
            if not stack:
                stack.append(num1)
                continue

            if stack[-1] == num1:
                continue

            if stack[-1] == num or num1 == num:
                stack = []
                temp_cnt += 1

        result = max(result, temp_cnt * 2)

    return result


print(solution([0, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 6, 7]))
print(solution([0, 3, 3, 0, 0, 2, 2, 0, 0, 2]))
print(solution([0, 0, 0, 2, 3, 4, 3, 5, 3, 1]))
print(solution([5, 0, 4, 2, 2, 9, 2, 6, 2, 7, 2]))
