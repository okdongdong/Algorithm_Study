N = int(input())
L = [int(i) for i in input().split()]
J = [int(i) for i in input().split()]

max_pleasure = 0

flags = ['0', '1']

for _ in range(N-1): # 모든 경우의 수 생성
    temp_flags = []
    for f in flags:
        for i in ['0', '1']:
            temp_flags.append(f + i)

    flags = temp_flags

for flag in flags:  # 모든 경우의 수에 대해 테스트 진행
    health = 100
    pleasure = 0

    for i in range(N):
        if flag[i]=='1':
            health -= L[i]
            pleasure += J[i]
            if health <= 0:
                break
            
    else:
        if max_pleasure < pleasure:
            max_pleasure = pleasure

print(max_pleasure)