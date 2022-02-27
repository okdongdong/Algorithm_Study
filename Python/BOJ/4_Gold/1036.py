N = int(input())
nums = [input() for _ in range(N)]
K = int(input())

num36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num36_diff = []
num_sum = 0
num_sep = []

# 문자열을 수정하기 위한 전처리 & 현재값들의 합 구함
for num in nums:
    temp = []
    temp.extend(num)
    num_sep.append(temp)
    num_sum += int(num, 36)

# 각 문자를 Z로 변경했을 때 합의 변화량을 구함
for k in num36:
    num_sum_diff = 0
    for num in num_sep:
        temp_str = ''
        for n in num:
            if n == k:
                temp_str += 'Z'
            else:
                temp_str += n
        num_sum_diff += int(temp_str, 36)
    num36_diff.append(num_sum_diff - num_sum)

# 최대값 == 기존값 + 최대 변화량
max_sum = num_sum + sum(sorted(num36_diff, reverse=True)[:K])

# 36진수로 변환
result = ''
while max_sum:
    result = num36[max_sum % 36] + result
    max_sum //= 36

print(result if result else '0')

# 완전탐색하다가 시간초과됨
# from itertools import combinations

# N = int(input())
# nums = [input() for _ in range(N)]
# K = int(input())
# if K == 36:
#     K -= 1

# from time import time
# s = time()

# num36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# num_sep = []
# num_sep_rev = []
# num_units = []

# max_len = 0
# for num in nums:
#     temp = []
#     temp.extend(num)
#     num_sep.append(temp)
#     num_sep_rev.append(temp[::-1])
#     if max_len < len(num):
#         max_len = len(num)


# for i in range(max_len):
#     temp = []
#     for num in num_sep_rev:
#         try:
#             temp.append(num[i])
#         except:
#             pass
#     num_units.append(sorted(temp,key=lambda x:(36-num36.index(x))*temp.count(x)))

# # 변경할 K개 문자 찾기
# K_nums = []
# K_lists = []
# num_comb = []
# for units in num_units[::-1]:
#     temp = []
#     for i in range(N):
#         try:
#             if (units[i] not in K_nums) and (units[i] != 'Z'):
#                 temp.append(units[i])
#         except:
#             break

#     temp = list(set(temp))
#     if len(temp) <= K:
#         K_nums += temp
#         K -= len(temp)

#     else:
#         num_comb = list(combinations(temp, K))
#         K = 0
#         for comb in num_comb:
#             K_lists.append(K_nums + list(comb))
#     if K == 0:
#         break

# if not K_lists:
#     K_lists = [K_nums]

# max_sum = 0
# for K_list in K_lists:
#     # K개의 문자를 Z로 변경
#     nums_sum = 0
#     for num in num_sep:
#         temp_str = ''
#         for n in num:
#             if n in K_list:
#                 temp_str += 'Z'
#             else:
#                 temp_str += n
#         nums_sum += int(temp_str, 36)
#     if max_sum < nums_sum:
#         max_sum = nums_sum

# # 36진수로 변환
# result = ''
# while max_sum:
#     result = num36[max_sum % 36] + result
#     max_sum //= 36

# # 결과출력
# print(result if result else '0')

# e = time()
# print(e-s)


#######################
# N = int(input())
# nums = [input() for _ in range(N)]
# K = int(input())

# num36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# num_sep = []
# num_sep_rev = []
# max_len = 0

# for num in nums:
#     temp = []
#     temp.extend(num)
#     num_sep.append(temp)
#     num_sep_rev.append(temp[::-1])
#     if max_len < len(num):
#         max_len = len(num)

# num_units = []

# for i in range(max_len):
#     temp = []
#     for num in num_sep_rev:
#         try:
#             temp.append(num[i])
#         except:
#             pass

#     num_units.append(sorted(temp,key=lambda x:(36-num36.index(x))*temp.count(x)))

# # 변경할 K개 문자 찾기
# K_list = []
# for units in num_units[::-1]:
#     for i in range(N):
#         try:
#             if units[i] not in K_list:
#                 K_list.append(units[i])
#                 K -= 1
#         except:
#             break
#         if K == 0:
#             break
#     if K == 0:
#         break

# # K개의 문자를 Z로 변경
# nums_sum = 0
# for num in num_sep:
#     temp_str = ''
#     for n in num:
#         if n in K_list:
#             temp_str += 'Z'
#         else:
#             temp_str += n
#     nums_sum += int(temp_str,36)

# # 36진수로 변환
# result = ''
# while nums_sum:
#     result = num36[nums_sum%36] + result
#     nums_sum //= 36

# # 결과출력
# print(result if result else '0')
