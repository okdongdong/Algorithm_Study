T = int(input())
for _ in range(T):
    N = int(input())
    max_price = 0
    max_name = ''
    for __ in range(N):
        price, name = input().split()
        price = int(price)
        if price > max_price:
            max_name = name
            max_price = price
    print(max_name)
