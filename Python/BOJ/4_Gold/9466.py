# 텀 프로젝트

T = int(input())
results = []
for _ in range(T):
    N = int(input())
    students = [0] + list(map(int, input().split()))
    check = [False] * (N+1)
    result = N

    for i in range(1, N+1):
        if check[i]:  
            continue
        
        check[i] = True

        if students[i] == i:
            result -= 1
            continue

        stack = [(i,students[i])]
        while True:
            next_i = stack[-1][1]
            
            if check[next_i]:
                break
            
            check[next_i] = True
            stack.append((next_i,students[next_i]))
        
        for idx in range(len(stack)):
            if stack[-1][1] == stack[idx][0]:
                result -= len(stack) -idx
                break
        
    results.append(result)

print(*results, sep='\n')
