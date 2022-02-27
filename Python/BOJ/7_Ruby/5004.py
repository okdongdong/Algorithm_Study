N, R = map(int, input().split())
A_B_lst =  []
price_lst = []
for i in range(R):
    A, B, price = map(int, input().split())
    A_B_lst.append([A, B])
    price_lst.append(price)
F = int(input())
