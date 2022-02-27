T = int(input())

for tc in range(T):
    N = int(input())
    result=0
    for i in range(N+1):
        if i%2:
            result += i
        else:
            result -= i
    print(f'#{tc+1} {result}')