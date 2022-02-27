### 맞은 코드
N = int(input())
cnt = 0
pre_list = [N]

if N == 1:  # N이 1일 경우 연산할 필요가 없으므로 0출력
    print(0)

else:       # 3가지 방법을 이용하는 경우의 수를 모두 탐색
    while True:

        cnt += 1
        now_list = []

        for num in pre_list:
            if num % 3 == 0:            # 1번 연산
                now_list.append(num // 3)

            if num % 2 == 0:            # 2번 연산
                now_list.append(num // 2)

            now_list.append(num - 1)    # 3번 연산
                
        if 1 in now_list: # 연산의 결과가 1이 되는 순간 while문 탈출
            break

        pre_list = list(set(now_list)) # 중복된 값을 제거

    print(cnt)


# ###재귀 -> 시간 초과
# def make_one(n):
#     n1, n2, n3 = 10**6, 10**6, 10**6
#     if db[n] != 0:
        
#         return db[n]
    
#     if n < 4:
#         return 1
    
#     else: 
#         if n % 3 == 0:
#             n3 = make_one(n // 3)

#         if n % 2 == 0:
#             n2 = make_one(n // 2)

#         n1 = make_one(n - 1) 

#         db[n] = min(n1, n2 , n3) + 1

#         return db[n]


# N = int(input())        
# db = [0 for _ in range(N+2)]
# print(make_one(N))