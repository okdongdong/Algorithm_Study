# M, N = map(int, input().split())
# nums = []

# for num in range(M, N + 1):
#     if num == 1:
#         continue
#     A = True
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             A = False
#             break
#     if A:
#         nums.append(num)

# print(*nums, sep='\n')


###########

M, N = map(int, input().split())
prime_list = [1]*(N+1)
prime_list[0] = 0
prime_list[1] = 0
nums = []
for i in range(2, N+1):
    for j in range(2*i, N+1, i):
        prime_list[j] = 0

for i in range(M, N+1):
    if prime_list[i]:
        nums.append(i)

print(*nums, sep='\n')