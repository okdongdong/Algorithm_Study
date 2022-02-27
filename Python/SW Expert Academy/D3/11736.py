T = int(input())

for t in range(T):
    N = int(input())
    lst = [int(i) for i in input().split()]
    cnt = 0
    for p in range(1, N - 1):
        if (lst[p-1] < lst[p] < lst[p+1]) or (lst[p+1] < lst[p] < lst[p-1]):
            cnt += 1
    print(f'#{t + 1} {cnt}')
