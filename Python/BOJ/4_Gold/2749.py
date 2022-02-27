# 피보나치 수 3

N = int(input())
# ※ 1000000으로 나눈 나머지의 경우 1500000을 주기로 반복됨
N %=1500000
p = 1000000
memo = [0] * (N+3)
memo[1] = 1
memo[2] = 1
for i in range(2, N+1):
    memo[i] = (memo[i-1] + memo[i-2]) % p

print(memo[N])


# N = int(input())
# p = 1000000
# memo = [0] * int(p*2)
# memo[1] = 1
# memo[2] = 1
# for i in range(2, p*2):
#     memo[i] = (memo[i-1] + memo[i-2]) % p

# # p로 나눈 나머지가 일정주기로 반복될거 같다는 생각으로 품
# # ※ 1000000으로 나눈 나머지의 경우 1500000을 주기로 반복됨

# for i in range(1, p*2):
#     if memo[i] == 0 and memo[i+1] == 1:
#         N %= i

# print(memo[N])
