def star(n, _r, _c, _flag):
    if n == 1:
        if _flag:
            arr[_r][_c] = ' '

        return

    for r in range(3):
        for c in range(3):
            flag = _flag or (r == 1 and c == 1)
            star(n//3, _r*3+r, _c*3+c, flag)


N = int(input())

arr = [['*']*N for _ in range(N)]

star(N, 0, 0, False)

for i in range(N):
    print(''.join(arr[i]))
