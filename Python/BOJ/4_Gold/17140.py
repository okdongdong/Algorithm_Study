# 이차원 배열과 연산

# 배열의 인덱스 1부터 시작, 1초마다 배열연산
# R연산 : R >= C, 행에 대해서 정렬
# C연산 : R < C, 열에 대해서 정렬
# 개수 => 숫자 순으로 오름차순 정렬
# 숫자, 개수, 숫자, 개수 순으로 작성
# 수를 정렬할 때 0 은 무시
# 배열의 크기는 최대 100
# 배열에 들어있는 숫자는 100이하 자연수


tr, tc, k = map(int, input().split())   # target_r, target_c, k
arr = [[0]*100 for _ in range(100)]
R, C = 3, 3
for r in range(R):
    temp = list(map(int, input().split()))
    for c in range(C):
        arr[r][c] = temp[c]


for time_cnt in range(101):
    if arr[tr-1][tc-1] == k:
        result = time_cnt
        break

    # R연산
    if R >= C:
        for r in range(R):
            cnt_dict = {}
            # 개수 카운트
            for c in range(C):
                if arr[r][c]:
                    try:
                        cnt_dict[arr[r][c]] += 1
                    except:
                        cnt_dict[arr[r][c]] = 1
            # 정렬
            temp_list = []
            for num, cnt in cnt_dict.items():
                temp_list.append((cnt, num))
            
            temp_list.sort()
            temp_C = 100 if len(temp_list) > 50 else len(temp_list)*2

            for c in range(temp_C//2):   # 숫자, 카운트 <- 카운트, 숫자
                arr[r][2*c] = temp_list[c][1] 
                arr[r][2*c+1] = temp_list[c][0]

            for c in range(temp_C, 100):
                arr[r][c] = 0
        
            if temp_C > C:
                C = temp_C

    # C연산
    else:
        for c in range(C):
            cnt_dict = {}
            # 개수 카운트
            for r in range(R):
                if arr[r][c]:
                    try:
                        cnt_dict[arr[r][c]] += 1
                    except:
                        cnt_dict[arr[r][c]] = 1
            # 정렬
            temp_list = []
            for num, cnt in cnt_dict.items():
                temp_list.append((cnt, num))
            
            temp_list.sort()
            temp_R = 100 if len(temp_list) > 50 else len(temp_list)*2
            for r in range(temp_R//2):   # 숫자, 카운트 <- 카운트, 숫자
                arr[2*r][c] = temp_list[r][1] 
                arr[2*r+1][c] = temp_list[r][0]

            for r in range(temp_R, 100):
                arr[r][c] = 0

            if temp_R > R:
                R = temp_R
else:
    result = -1

print(result)