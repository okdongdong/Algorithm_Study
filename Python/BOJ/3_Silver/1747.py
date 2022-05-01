N = int(input())
prime_num = []
prime_check = [False]*N
prime_check[0] = True
result = 2
if N > 1:
    prime_check[1] = True

    for i in range(2, N):
        if prime_check[i]:
            continue

        prime_num.append(i)

        for j in range(i+i, N, i):
            prime_check[i] = True

    num = N
    while True:
        number = str(num)
        for j in range(len(number)//2):
            if number[j] != number[len(number)-1-j]:
                break

        else:
            for i in prime_num:
                if not num % i:
                    break
            else:
                result = num
                break

            prime_num.append(i)

        num += 1

print(result)
