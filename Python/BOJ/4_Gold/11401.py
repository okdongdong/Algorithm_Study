# 이항 계수 3
def cal_p(denom, _p):
    global p
    if not memo.get(_p):
        if _p < 2:
            memo[_p] = (denom**_p) % p

        elif _p % 2:
            memo[_p] = (cal_p(denom, _p-1) * denom) % p

        else:
            memo[_p] = (cal_p(denom, _p//2)**2) % p

    return memo[_p]


N, K = map(int, input().split())
p = 1000000007
nums = [1]*4000001
for i in range(1, N+1):
    nums[i] = nums[i-1]*i
    nums[i] %= p

memo = dict()

denom = (nums[N-K]*nums[K]) % p
result = (nums[N] * cal_p(denom, p-2)) % p

print(result)

# 페르마 소정리
# a, p 가 서로소이고, p는 소수일 때
# 1. a^p === a (mod p)
# 2. a^(p-1) === 1 (mod p)
# 3. a^(p-2) === 1/a (mod p)
