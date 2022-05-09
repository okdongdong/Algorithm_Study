## 제곱 ㄴㄴ

def cal_multi_prime_comb(num, cnt, start_i):
    if num > 2e9 or cnt > 6 or num in multi_prime_comb_list[cnt]:
        return

    if num > 1:
        multi_prime_comb_list[cnt].add(num)

    for i in range(start_i+1, len(prime_square_nums)):
        if num*prime_square_nums[i] > 2e9:
            return

        cal_multi_prime_comb(num, cnt, i)
        cal_multi_prime_comb(num*prime_square_nums[i], cnt+1, i)


# N == K + N보다 작은 제곱 ㄴㄴ수의 개수
def recursion(K, diff=0):

    next_diff = 0
    for i in range(6):
        for num in multi_prime_comb_list[i]:
            temp = K//num * (-1)**i

            if not temp:
                break

            next_diff += temp

    next_K = K + next_diff - diff

    if next_K == K:
        return K

    return recursion(next_K, next_diff)


K = int(input())
# 예제 4번을 통해서 10억번째 제곱 ㄴㄴ수가 20억 보다 작다고 가정
upper_bound = 44722   # 2,000,000,000 ** .5 = 44,721.35954999579...
nums = [1] * upper_bound
prime_square_nums = []

# 제곱수 계산
for i in range(2, upper_bound-1):
    if not nums[i]:
        continue

    prime_square_nums.append(i**2)

    for j in range(i+i, upper_bound, i):
        nums[j] = 0


# 제곱수의 곱으로 만들 수 있는 20억보다 작은 수 계산
multi_prime_comb_list = [set() for _ in range(6)]  # 가장작은 제곱수 7개의 곱 > 20억

for i in range(len(prime_square_nums)):
    cal_multi_prime_comb(prime_square_nums[i], 0, i)

for i in range(6):
    multi_prime_comb_list[i] = sorted(list(multi_prime_comb_list[i]))

print(recursion(K))
