# 구구단1

def isGugudan(n):

    if (n > 81) or (n < 1):
        return "No"
    else:
        for i in range(1,10):
            if n/i in range(1,10):
                return "Yes"
        return "No"

N = int(input())

for i in range(N):
    yn = isGugudan(int(input()))
    print(f'#{i+1} {yn}')
