T = int(input())

for t in range(T):
    S = input()
    cnt = []
    for s in S:
        cnt.append(S.count(s))
    if cnt == [2,2,2,2]:
        result = 'Yes'
    else:
        result = 'No'
    print(f'#{t + 1} {result}')

