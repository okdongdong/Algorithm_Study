import sys
input = sys.stdin.readline

while True:
    N = int(input())

    if not N:
        break

    money_list = []
    for i in range(N):
        now_money = int(input())
        if i:
            money_list.append(max(now_money, money_list[-1]+now_money))
        else:
            money_list.append(now_money)

    print(max(money_list))
