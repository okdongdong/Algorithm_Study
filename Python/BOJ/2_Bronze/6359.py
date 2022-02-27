T = int(input())


for tc in range(T):
    n = int(input())
    room_lst = [False for _ in range(n)]

    for k in range(1, n+1):
        for i in range(k-1, n, k):
            room_lst[i] = not(room_lst[i])
    
    print(sum(room_lst))