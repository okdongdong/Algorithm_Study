T = int(input())
a, T = divmod(T, 300)
b, T = divmod(T, 60)
c, T = divmod(T, 10)
if T:
    print(-1)
else:
    print(a, b, c)
