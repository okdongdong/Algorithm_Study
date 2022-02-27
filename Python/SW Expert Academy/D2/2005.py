def pascal(n):
    if n == 1:
        lst = [1]
        return lst

    elif n == 2:
        lst = [1, 1]
        return lst

    else:
        lst = [1]
        pre_lst = pascal(n - 1)
        for i in range(n - 2):
            lst.append(int(pre_lst[i]) + int(pre_lst[i + 1]))
        lst.append(1)
        return lst


T = int(input())

for i in range(T):
    N = int(input())
    print(f'#{i+1}')
    for j in range(1, N+1):
        print(*pascal(j), sep=' ')