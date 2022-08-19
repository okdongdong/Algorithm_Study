T = int(input())
prime = []
check = [False]*10000
for i in range(2, 10000):
    if check[i]:
        continue

    prime.append(i)

    for j in range(i+i, 10000, i):
        check[j] = True

for _ in range(T):
    N = int(input())
    for a in range(N//2, N):
        b = N-a
        if a in prime and b in prime:
            break
    print(b, a)
