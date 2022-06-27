# 완전제곱수

square_nums = set([i**2 for i in range(1, 101)])

M = int(input())
N = int(input())
a = 0
b = 0
for num in range(M, N+1):
    if num in square_nums:
        a += num
        if b:
            continue
        b = num

if b:
    print(a)
    print(b)
else:
    print(-1)
