# μνΈμ μ
P, K = map(int, input().split())
for num in range(2, K):
    if P % num == 0:
        print("BAD", num)
        break
else:
    print("GOOD")
