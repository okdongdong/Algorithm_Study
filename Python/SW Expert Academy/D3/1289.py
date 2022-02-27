# 0과 1이 서로 전환되는 횟수를 구하는 문제

T = int(input())
for tc in range(1,T+1):
    memory = input()
    flag = True     # 플래그를 통해 이전 숫자가 1인지, 0인지 판단, 0: True, 1: False 
    cnt = 0        # 숫자 전환 횟수 카운트
    for bit in memory:
        if bit == '1' and flag:
            cnt += 1
            flag = False

        elif bit == '0' and not flag:
            cnt +=1
            flag = True
            
    print('#{} {}'.format(tc, cnt))
        