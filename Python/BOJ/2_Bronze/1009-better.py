T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    a = a % 10  # a의 1의 자리 수만 취함

    if a == 0:
        print(10)
    else:
        lst = [a]
        i = 2
        while 1:
            if a == a ** i % 10:
                break
            lst.append(a ** i % 10)
            i += 1
        a = lst.pop()
        lst.insert(0, a)
        print(lst[b % len(lst)])
