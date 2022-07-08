# 마법의 구슬
S, F, M = map(int, input().split())
prime_check = [True] * (M+1)
prime_check[0], prime_check[1] = False, False

for i in range(2, M+1):
    if not prime_check[i]:
        continue

    for j in range(i+i, M+1, i):
        prime_check[j] = False

prime_nums = []
for i in range(2, M+1):
    if prime_check[i]:
        prime_nums.append(i)

sfCs = 1

SF = S+F
for prime in prime_nums:
    num = prime
    temp = 0
    while num <= SF:

        temp += SF//num - S//num - F//num
        num *= prime

    sfCs *= prime**temp

for i in range(M, 0, -1):
    if not sfCs % i:
        print(i)
        break
