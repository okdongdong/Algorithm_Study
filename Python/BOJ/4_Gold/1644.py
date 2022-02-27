# 소수의 연속합

N = int(input())

prime_num = [True]*(N+1)
prime_num[0] = False
prime_num[1] = False

# 소수 리스트 생성
for n in range(2, int(N**0.5)+1):
    if not prime_num[n]:
        continue
    for m in range(2*n, N+1, n):
        prime_num[m] = False

number = []
for i in range(2, N+1):
    if prime_num[i]:
        number.append(i)

left = 0
right = 0
cnt = 0
prime_sum = 0
while left < len(number):
    if prime_sum == N:
        cnt += 1
        prime_sum -= number[left]
        left += 1
        if right < len(number):
            prime_sum += number[right]
            right += 1

    elif prime_sum < N and right < len(number):
        prime_sum += number[right]
        right += 1

    else:
        prime_sum -= number[left]
        left += 1

print(cnt)
