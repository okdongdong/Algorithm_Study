# 양궁대회

def cal_diff(apeach_info, lion_info):
    diff = 0
    for i in range(10):
        if lion_info[i] > apeach_info[i]:
            diff += 10-i
        elif apeach_info[i] and lion_info[i] <= apeach_info[i]:
            diff -= 10-i
    return diff


def cal(n, apeach_info, lion_info, i=0):
    global max_diff, answer

    if n == 0 or i == 10:
        lion_info[10] = n
        now_diff = cal_diff(apeach_info, lion_info)
        if max_diff < now_diff:
            max_diff = now_diff
            answer = lion_info[:]
        elif max_diff == now_diff:
            answer = sorted((answer, lion_info[:]), key=lambda x:x[::-1])[1]
        return

    if n > apeach_info[i]:
        lion_info[i] = apeach_info[i] + 1
        cal(n - lion_info[i], apeach_info, lion_info, i+1)
        lion_info[i] = 0
    cal(n, apeach_info, lion_info, i+1)


def solution(n, info):
    global max_diff, answer
    now_info = [0] * 11
    max_diff = 0
    answer = []

    cal(n, info, now_info)

    if max_diff <= 0:
        answer = [-1]

    return answer


print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))




# def cal_diff(apeach_info, lion_info):
#     diff = 0
#     for i in range(10):
#         if lion_info[i] > apeach_info[i]:
#             diff += 10-i
#         elif apeach_info[i] and lion_info[i] <= apeach_info[i]:
#             diff -= 10-i
#     return max(0, diff)


# def cal(n, apeach_info, lion_info, now_round=0):
#     global max_diff, answer, check

#     if n == now_round:
#         now_diff = cal_diff(apeach_info, lion_info)
#         if max_diff < now_diff:
#             max_diff = now_diff
#             answer = lion_info[:]
#         return

#     for i in range(11):
#         if i != 10 and check[i]:
#             continue

#         lion_info[i] += 1
#         if lion_info[i] > apeach_info[i]:
#             check[i] = True
#         cal(n, apeach_info, lion_info, now_round + 1)
#         lion_info[i] -= 1
#         check[i] = False


# def solution(n, info):
#     global max_diff, answer, check
#     check = [False] * 11
#     now_info = [0] * 11
#     max_diff = 0
#     answer = []

#     cal(n, info, now_info)

#     if not max_diff:
#         answer = [-1]

#     return answer


# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
