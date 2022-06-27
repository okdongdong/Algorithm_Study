# 화성 수학
T = int(input())
for _ in range(T):
    expression_list = input().split()
    num = float(expression_list[0])
    for i in range(1, len(expression_list)):
        operator = expression_list[i]
        if operator == '@':
            num *= 3
        elif operator == '%':
            num += 5
        else:
            num -= 7
    print(f'{num:0.2f}')
