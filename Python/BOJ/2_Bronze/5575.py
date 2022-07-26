# 타임카드
for _ in range(3):
    a1, b1, c1, a2, b2, c2 = map(int, input().split())
    b, c = divmod(c2-c1, 60)
    a, b = divmod(b2-b1+b, 60)
    a += a2-a1
    print(a, b, c)
