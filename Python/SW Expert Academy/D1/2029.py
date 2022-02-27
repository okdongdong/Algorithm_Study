N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    result = divmod(a,b)
    print(f'#{i+1} {result[0]} {result[1]}')