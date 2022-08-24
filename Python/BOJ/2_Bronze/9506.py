while True:
    n = int(input())
    if n == -1:
        break

    divisors = [1]

    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    if sum(divisors) != n:
        print(f'{n} is NOT perfect.')
        continue

    divisors.sort()
    print(f'{n} = {" + ".join(map(str, divisors))}')
