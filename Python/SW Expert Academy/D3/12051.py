# 프리셀 통계
def free_stat(N, p_D, p_G):
    if (p_D != 100) and (p_G == 100):
        return "Broken"
    elif (p_D != 0) and (p_G == 0):
        return "Broken"
    else:
        if N == 1 and p_D not in [0, 100]: pass
        elif N < 4 and p_D not in [0, 50, 100]: pass
        elif N < 5 and p_D not in [0, 25, 50, 75, 100]: pass
        elif N < 10 and p_D not in [0, 25, 50, 75, 100, 20,40,60,80]: pass
        elif N < 20 and p_D not in [0, 25, 50, 75, 100, 10,20,30,40,60,70,80,90]: pass
        elif N < 25 and p_D not in list(range(0,101,5))+[0, 25, 50, 75, 100, 10,20,30,40,60,70,80,90]: pass
        elif N < 50 and p_D not in list(range(0,101,4))+list(range(0,101,5))+[0, 25, 50, 75, 100, 10,20,30,40,60,70,80,90]: pass
        elif N < 100 and p_D not in list(range(0,101,2))+list(range(0,101,4))+list(range(0,101,5))+[0, 25, 50, 75, 100, 10,20,30,40,60,70,80,90]: pass
        else:
            return "Possible"
        return "Broken"

n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    PorB = free_stat(a, b, c)
    print(f'#{i + 1} {PorB}')

# 코드 정리가 필요해 보입니다.

