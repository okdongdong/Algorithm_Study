T = int(input())
for i in range(T):
    txt = input()
    if txt == txt[::-1]:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')