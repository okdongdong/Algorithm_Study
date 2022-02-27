# 파이썬이 지원이 안되네

N = int(input())

for i in range(N):
    num = int(input())
    cnt = 0
    while num > 10:
        cnt += 1
        num /= 10

    num = round(num,1)

    if num >= 10:
        cnt += 1
        num /= 10

    print(f'{i+1} {num}*10^{cnt}')