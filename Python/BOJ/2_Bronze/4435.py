N = int(input())

result = [
    'Evil eradicates all trace of Good',
    'Good triumphs over Evil',
    'No victor on this battle field'
]

a_score = [1, 2, 3, 3, 4, 10]
b_score = [1, 2, 2, 2, 3, 5, 10]

for i in range(N):
    a = sum(map(lambda x: int(x[0])*x[1], zip(input().split(), a_score)))
    b = sum(map(lambda x: int(x[0])*x[1], zip(input().split(), b_score)))

    if a < b:
        c = 0
    elif a > b:
        c = 1
    else:
        c = 2

    print(f'Battle {i+1}: {result[c]}')
