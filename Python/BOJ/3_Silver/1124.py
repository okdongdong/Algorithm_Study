# 언더프라임

from time import time
import sys

A, B = map(int, sys.stdin.readline().split())

s = time()

lst = [1]*100001                            # 소수를 판별 & 소인수의 수 저장
lst[0], lst[1] = 0, 0                       

# 소수판별, 에라토스테네스의 체
for i in range(2, 100001):
    n = 2
    while i*n < 100001:
        lst[i*n] = 0
        n += 1

# 소인수분해를 위햔 소수리스트 생성
prime_lst = []                              # 소수를 저장할 리스트
for idx, val in enumerate(lst):
    if val == 1:
        prime_lst.append(idx)

# 소인수의 수 계산
result = 0
for num in range(A, B+1):
    temp = num
    temp_lst = []                           # 모든 약수에 대한 소인수의 수를 계산하기 위한 임시저장 리스트
    cnt, n = 0, 0                           # 소인수 개수 / 소수인덱스
    
    if lst[temp] == 1:                      # 현재 수가 소수일 경우, 소인수의 수 == 1이므로 계산하지 않음
        continue

    # 소인수 분해
    while temp > 1:
        if lst[temp]:                       # memoization 활용
            cnt += lst[temp]                # 소인수의 수 저장 리스트에 값이 있을 경우 값을 불러와 활용
            temp = 1                        # 반복문 바로 탈출
        
        else:
            if temp % prime_lst[n]:         # 안나눠질 경우 다음 소수로 이동
                n += 1                      
            
            else:                           # 나눠지는 경우
                temp_lst.append(temp)       # 모든 약수에 대한 소인수의 수를 계산하기 위해 임시저장
                temp //= prime_lst[n]
                cnt += 1                    # 나눠질 때마다 소인수 개수 +1

    for idx, val in enumerate(temp_lst):    # 계산과정에서의 모든 약수에 대한 소인수의 수 저장
        lst[val] = cnt - idx                # 계산순서대로, 큰수 -> 작은수로 저장

    if lst[cnt] == 1:                       # 소인수의 수가 소수일 경우, 결과값 추가
        result += 1

print(result)

e = time()

print(e-s)