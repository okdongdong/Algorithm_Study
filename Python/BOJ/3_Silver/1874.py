# 스택 수열
import sys
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
now_num = 1
stack = []
result = []
flag = False

for num in nums:
    while now_num <= num:
        result.append('+')
        stack.append(now_num)
        now_num += 1

    if stack and stack[-1] == num:
        result.append('-')
        stack.pop()
    
    else: 
        result = ['NO']
        break

print(*result, sep='\n')













# # 스택 수열
# import sys
# input = sys.stdin.readline
# N = int(input())
# num_squence = [int(input()) for _ in range(N)]
# nums = list(range(N,0,-1))
# flag = False
# stack = []
# result = []
# for num in num_squence:
#     while nums:
#         temp = nums[-1]
#         if temp == num:
#             nums.pop()
#             result.append('+')
#             result.append('-')
#             break

#         elif temp < num:
#             nums.pop()
#             result.append('+')
#             stack.append(temp)

#         else:
#             if stack and stack[-1] == num:
#                 result.append('-')
#                 stack.pop()
#                 break

#             else:
#                 flag = True
#                 break
#     else:
#         if stack and stack[-1] == num:
#             result.append('-')
#             stack.pop()
#         else:
#             flag = True
    
#     if flag:
#         break

# if flag:
#     result = ['NO']

# print(*result, sep='\n')
