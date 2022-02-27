# 오큰수

N = int(input())
nums = list(map(int, input().split()))
stack = []
result = [-1]*N
for i in range(N):
    while stack and nums[i] > stack[-1][0]:
        num, idx = stack.pop()
        result[idx] = nums[i]
    stack.append((nums[i],i))
    
print(*result)