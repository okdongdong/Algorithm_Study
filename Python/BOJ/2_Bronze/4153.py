# 직각삼각형
while True:
    abc = list(map(int, input().split()))
    abc.sort()
    a, b, c = abc
    if a==0:
        break
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')