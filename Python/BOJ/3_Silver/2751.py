# 수 정렬하기 2

import sys
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
nums_check = [0]*2000001
result = []
for n in nums:
    nums_check[n+1000000] = 1

for i in range(2000001):
    if nums_check[i]:
        result.append(i-1000000)
print(*result,sep='\n')

# import sys
# input = sys.stdin.readline
# N = int(input())
# nums = [int(input()) for _ in range(N)]
# nums.sort()
# print(*nums,sep='\n')
