import sys    # 인풋에 처리해줘도 이게 더 빠르네
input = sys.stdin.readline
A = input()[:-1]    # rstrip보다 이게 빠름
B = input()[:-1]

# B 전처리
B_dic = {}
for i in range(len(B) - 1):
    B_dic[B[i]] = len(B) - i - 1

for i in range(len(B) - 2, -1, -1):
    for j in range(i + 1):
        if B[j] != B[len(B) - i - 1 + j]:
            break
    else:
        KMP = len(B) - i - 1
        break
else:
    KMP = len(B)

# A 탐색
cnt = 0
A_idx = 0
A_idx_list = []
kmp_s = -1
while A_idx < len(A) - len(B) + 1:
    for i in range(len(B) - 1, kmp_s, -1):
        if B[i] != A[A_idx + i]:
            try:
                A_idx += B_dic[A[A_idx + len(B) - 1]]

            except:
                A_idx += len(B)

            kmp_s = -1
            break

    else:
        cnt += 1
        A_idx_list.append(A_idx + 1)
        A_idx += KMP               # 앞부분과 동일한 부분이 겹치게끔 이동
        kmp_s = len(B) - KMP - 1   # 앞부분과 동일한 부분은 검사하지 않게 범위 조정

print(cnt)
print(*A_idx_list)



# A = input()
# B = input()

# # B 전처리
# B_dic = {}
# for i in range(len(B) - 1):
#     B_dic[B[i]] = len(B) - i - 1

# for i in range(len(B) - 2, -1, -1):
#     for j in range(i + 1):
#         if B[j] != B[len(B) - i - 1 + j]:
#             break
#     else:
#         KMP = len(B) - i - 1
#         break
# else:
#     KMP = len(B)

# # A 탐색
# cnt = 0
# A_idx = 0
# A_idx_list = []
# kmp_s = -1
# while A_idx < len(A) - len(B) + 1:
#     for i in range(len(B) - 1, kmp_s, -1):
#         if B[i] != A[A_idx + i]:
#             try:
#                 A_idx += B_dic[A[A_idx + len(B) - 1]]

#             except:
#                 A_idx += len(B)

#             kmp_s = -1
#             break

#     else:
#         cnt += 1
#         A_idx_list.append(A_idx + 1)
#         A_idx += KMP               # 앞부분과 동일한 부분이 겹치게끔 이동
#         kmp_s = len(B) - KMP - 1   # 앞부분과 동일한 부분은 검사하지 않게 범위 조정

# print(cnt)
# print(*A_idx_list)