n=int(input())
for i in range(n):
    result = sum(list(filter(lambda x: x%2!=0, map(int, input().split()))))
    print(f"#{i+1} {result}")