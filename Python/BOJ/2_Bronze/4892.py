# 숫자 맞추기 게임
idx = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break

    n1 = 3 * n0
    n2 = (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    is_odd = 'odd' if n1 % 2 else 'even'

    print(f'{idx}. {is_odd} {n4}')
    idx += 1
