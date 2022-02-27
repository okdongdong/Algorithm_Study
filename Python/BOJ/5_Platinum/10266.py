# 시계 사진들
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_list = [False]*360000
B_list = [False]*360000

# 숫자간의 간격을 표시
for i in range(N):
    A_list[A[i]] = True
    B_list[B[i]] = True

A = []
B = []

temp_A = 0
temp_B = 0

# 간격 패턴 리스트 생성
for i in range(360000):
    if A_list[i]:
        A.append(temp_A)
        temp_A = 0
    else:
        temp_A += 1

    if B_list[i]:
        B.append(temp_B)
        temp_B = 0
    else:
        temp_B += 1

A[0] += temp_A
B[0] += temp_B
A += A  # A뒤에 A를 붙혀서 순환하는 경우를 탐색
# 패턴 시연
# print(A, B)

# B전처리(일치하는 숫자를 맞추기 위해 몇칸을 움직여야 하는지 표시)
pattern_length = len(B)
B_dict = {}
for i in range(pattern_length-1):
    B_dict[B[i]] = pattern_length - i - 1
    print(B_dict)

# A 탐색(탐색은 B의 마지막부터 일치하는지 검사)
A_idx = 0   # 연장된 A패턴에서 탐색을 시작할 위치
kmp_s = -1  # 여기 전까지는 이미 일치하는 것을 확인
while A_idx < pattern_length:   # A패턴의 길이만큼만 검사, A패턴의 길이 == B패턴의 길이
    for i in range(pattern_length-1, kmp_s, -1):
        if B[i] != A[A_idx + i]:    # 패턴이 일치하지 않는다면
            try:    # B 패턴에 존재하는 숫자인 경우 그만큼 도약
                A_idx += B_dict[A[A_idx + pattern_length - 1]]
                kmp_s = - 1

            except:  # B 패턴에 존재하지 않는 숫자가 A에서 나오는 경우
                A_idx += 1000000    # while문 탈출 위해 큰 수 더함

            break

    else:   # 일치하는 숫자패턴이 있는 경우
        result = 'possible'
        break

else:   # A패턴의 길이만큼을 모두 탐색해도 패턴이 일치하지 않는 경우
    result = 'impossible'

print(result)


# # 시계 사진들
# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# A_list = [False]*360000
# B_list = [False]*360000

# # 숫자간의 간격을 표시
# for i in range(N):
#     A_list[A[i]] = True
#     B_list[B[i]] = True

# A = []
# B = []

# temp_A = 0
# temp_B = 0

# # 간격 패턴 리스트 생성
# for i in range(360000):
#     if A_list[i]:
#         A.append(temp_A)
#         temp_A = 0
#     else:
#         temp_A += 1

#     if B_list[i]:
#         B.append(temp_B)
#         temp_B = 0
#     else:
#         temp_B += 1

# A[0] += temp_A
# B[0] += temp_B
# A += A  # A뒤에 A를 붙혀서 순환하는 경우를 탐색
# # 패턴 시연
# # print(A, B)

# # B전처리(일치하는 숫자를 맞추기 위해 몇칸을 움직여야 하는지 표시)
# pattern_length = len(B)
# B_dict = {}
# for i in range(pattern_length-1):
#     B_dict[B[i]] = pattern_length - i - 1

# # A 탐색(탐색은 B의 마지막부터 일치하는지 검사)
# A_idx = 0   # 연장된 A패턴에서 탐색을 시작할 위치
# while A_idx < pattern_length:   # A패턴의 길이만큼만 검사, A패턴의 길이 == B패턴의 길이
#     for i in range(pattern_length-1, -1, -1):
#         if B[i] != A[A_idx + i]:    # 패턴이 일치하지 않는다면
#             try:    # B 패턴에 존재하는 숫자인 경우 그만큼 도약
#                 A_idx += B_dict[A[A_idx + pattern_length - 1]]

#             except:  # B 패턴에 존재하지 않는 숫자가 A에서 나오는 경우
#                 A_idx += 1000000    # while문 탈출 위해 큰 수 더함

#             break

#     else:   # 일치하는 숫자패턴이 있는 경우
#         result = 'possible'
#         break

# else:   # A패턴의 길이만큼을 모두 탐색해도 패턴이 일치하지 않는 경우
#     result = 'impossible'

# print(result)
