a = -int(input())+int(input())

if a <= 0:
    print('Congratulations, you are within the speed limit!')

else:
    if 0 < a <= 20:
        b = 100
    elif 20 < a <= 30:
        b = 270
    else:
        b = 500
    print(f'You are speeding and your fine is ${b}.')
