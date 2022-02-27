# 6190. 정곤이의 단조 증가하는 수

def is_danjo(n):
    n = str(n)
    for i in range(1, len(n)):
        if int(n[i-1]) > int(n[i]): # 앞의 수가 뒤의 수보다 큰경우, 단조증가가 아님
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    max_num = -1            # 최댓값 구해야 하고, 단조증가하는 수가 없다면 -1 출력해야 함
    for i in range(N-1):    # 문제에서 주어진 i,j의 범위를 반복, i,j는 인덱스 보정한 후 값임
        for j in range(i+1,N):  
            num = A[i]*A[j] 
            if is_danjo(num):       # 두 숫자의 곱이 단조증가하는 수인 경우
                if max_num < num:   # 최대값 구함
                    max_num = num

    print('#{} {}'.format(tc, max_num))