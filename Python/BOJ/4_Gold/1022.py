# 소용돌이 예쁘게 출력하기

def cal_value(r, c):
    if c != 0 and abs(r/c) < 1:
        if c < 0:
            val = ((2*c)**2 + 1) - (c-r)

        else:
            val = (2*c - 1)**2 + (c-r)

    else:
        if r < 0:
            val = ((2*r)**2 + 1)-(c-r)

        else:
            val = (2*r + 1)**2 + (c-r)

    return val


r1, c1, r2, c2 = map(int, input().split())

arr = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]

for r in range(r1, r2+1):
    for c in range(c1, c2+1):
        arr[r-r1][c-c1] = cal_value(r, c)

max_len = len(str(max(arr[0][0], arr[0][-1], arr[-1][-1], arr[-1][0])))

for a in arr:
    for num in a:
        print(str(num).rjust(max_len), end=' ')
    print()
