n=int(input())
for i in range(n):
    result = (lambda x: sum(x)/len(x))(list(map(int, input().split())))
    print(f"#{i+1} {result:0.0f}")