N = int(input())
towers = list(map(int, input().split()))
result = ['0']*N

stack = [(N-1, towers[N-1])]

for i in range(N-2, -1, -1):
    while stack and stack[-1][1] < towers[i]:
        idx, height = stack.pop()
        result[idx] = f'{i+1}'

    stack.append((i, towers[i]))

print(' '.join(result))
