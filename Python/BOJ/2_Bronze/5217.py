# 쌍의 합
T = int(input())
for _ in range(T):
    N = int(input())
    result = f'Pairs for {N}: '
    temp = []
    for i in range(1, (N+1)//2):
        temp.append(f'{i} {N-i}')

    print(result+', '.join(temp))
