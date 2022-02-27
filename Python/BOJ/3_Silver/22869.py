import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

if K >= (i-s)*(1+abs(A[s-1]-A[i-1])): # 가능










## 시간초과
# def small():
#     stone = [1]

#     while stone:
#         s = stone.pop()
#         for i in range(s+1, N+1):
#             if K >= (i-s)*(1+abs(A[s-1]-A[i-1])):
#                 stone.append(i)
        
#         if N in stone:
#             return 'YES'

#     return 'NO'

# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# print(small())