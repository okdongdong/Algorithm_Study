# 서든어택 3

N = int(input())
A_i = list(map(int, input().split()))
me = A_i[0]
A_i = A_i[1:]

result = 'Yes'

while A_i:              # 적이 존재하는 한 반복
    over_me = []
    under_me = []
    
    for a in A_i:
        if a < me:
            under_me.append(a)
        else:
            over_me.append(a)

    if not under_me:    # 공격력이 낮은 적이 없다 == 죽일수가 없다 == 최후의 생존자 불가
        result = 'No'
        break

    me += sum(under_me) # 내가 죽일 수 있는 적들을 모두 죽임
    A_i = over_me       # 새로운 적들

print(result)
