T = int(input())

for i in range(T):
    txt = input()
    
    for n in range(1,10):
        if txt[:n] == txt[n:2*n]:
            print(f'#{i+1} {n}')
            break