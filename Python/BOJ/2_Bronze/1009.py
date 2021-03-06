T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    a = a % 10  # a의 1의 자리 수만 취함

    if a == 0:
        print(10)

    elif a in [1, 5, 6]:
        print(a)

    elif a in [4, 9]:
        if b % 2:
            print(a)
        else:
            print((a * a) % 10)
    else:
        lst = [a ** 4 % 10, a, a ** 2 % 10, a ** 3 % 10]    # 인덱스 접근성을 위한 lst 배치
        print(lst[b % 4])                                   # 4개 숫자 반복

'''       
    1 -> 1, 1, 1, ...
    2 -> 2, 4, 8, 6, 2, ...
    3 -> 3, 9, 7, 1, 3, ...
    4 -> 4, 6, 4, ...
    5 -> 5, 5, 5, ...
    6 -> 6, 6, 6, ...
    7 -> 7, 9, 3, 1, 7, ...
    8 -> 8, 4, 2, 6, 8, ...
    9 -> 9, 1, 9, ...
    0 -> 0, 0, 0, ...
'''
