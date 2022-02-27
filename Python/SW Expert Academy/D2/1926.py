N = int(input())
cnt = 0
for i in range(1, N + 1):
    for j in str(i):
        if j in ['3', '6', '9']:
            cnt += 1
    if cnt > 0:
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')
    cnt = 0
