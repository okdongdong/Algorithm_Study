import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a_list = list(map(int, input().split()))    # a: 출제자 번호
b_list = list(map(int, input().split()))    # b: 준비시간
ab_list = list(zip(a_list, b_list))
result = []

arr = [[] for _ in range(N+1)]

for a, b in ab_list:
    arr[a].append(b)

for L in range(1, N+1):
    for a in a_list:
        arr[a]

    else:
        temp = -1

    result.append(temp)

print(*result)


# 65짜리 답2 시간은 좀 덜걸림
# 정렬이 원인인 것 같음

# N, K = map(int, input().split())

# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))

# ab_list = sorted(list(zip(a_list, b_list)))
# result = []

# for L in range(1, N+1):
#     temp_list = []
#     for a, b in ab_list:
#         if a_temp == a:
#             if cnt == L:
#                 continue
#             else:
#                 cnt += 1
#                 temp_list.append(b)

#         else:
#             a_temp = a
#             cnt = 1
#             temp_list.append(b)

#     if len(temp_list) < K:
#         temp = -1

#     else:
#         temp = sum(sorted(temp_list)[:K])

#     result.append(temp)

# print(*result)




# # 65점짜리 답
# N, K = map(int, input().split())
# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))

# ab_list = sorted(list(zip(a_list,b_list)),key=lambda x : x[1])

# result = []
# for L in range(1,N+1):
#     a_used = []
#     a_cnt = {}
#     temp, cnt = 0, 0
#     for a, b in ab_list:
#         if a not in a_used:   # a가 L개 사용되면 a_used에 넣음
#             try:
#                 a_cnt[a] += 1

#             except:
#                 a_cnt[a] = 1

#             if a_cnt.get(a) == L:
#                     a_used.append(a)

#             temp += b
#             cnt += 1

#         if cnt == K:
#             break

#     else:
#         temp = -1

#     result.append(temp)

# print(*result)
