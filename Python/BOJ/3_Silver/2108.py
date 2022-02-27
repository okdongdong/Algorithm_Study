import sys

input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]

num_sum = 0                 # 평균을 구하기 위한 합
num_min = nums[0]           # 최대 최소 차이를 구하기 위한 최소값
num_max = nums[0]           # 최대값
num_dic = {}                # 최빈값, 중앙값을 구하기 위한 딕셔너리

for num in nums:            # 숫자를 돌면서 숫자별 개수, 숫자합, 최대값, 최솟값 구함
    try:                    # 숫자별 개수
        num_dic[num]+=1
    except:
        num_dic[num]=1

    num_sum += num          # 숫자합

    if num > num_max:       # 최대값
        num_max = num
    elif num < num_min:     # 최소값
        num_min = num

num_lst = sorted(num_dic.items())   # 이거는 최대 8000개 정렬이라서 시간 오래 안걸림
ismedian,isodd = divmod(N,2)        # 밑에 for문안에서 연산량을 줄일려고 몫과 나머지 미리구해줌
cnt = 0                             # 중앙값 찾기위한 누적 카운트
median_flag = True                  # 찾은 중앙값을 갱신하지 않기 위한 flag
max_mode_cnt = 0                    # 최빈수의 개수
min_mode_num = 4001                 # 숫자 범위가 4000을 넘지 않으므로 4001로 설정
snd_mode_num = 4001

for num, num_cnt in num_lst: 
    cnt += num_cnt
    
    if median_flag and cnt > ismedian:  # 누적 카운트가 N//2를 를 넘는 순간 == 중앙값
        num_median = num
        median_flag = False             # 추가적 갱신을 막기위한 flag
    
    if num_cnt > max_mode_cnt:          # 최빈값 개수비교
        max_mode_cnt = num_cnt
        min_mode_num = num              # 최빈값 계산
        snd_mode_num = 4001             # 최빈값 중 두번째로 작은 값

    elif num_cnt == max_mode_cnt:       # 최빈값이 같은게 있다면
        if snd_mode_num > num > min_mode_num:   # 최빈값 중 두번쨰로 작은지 확인
            snd_mode_num = num
        elif num < min_mode_num:    
            snd_mode_num = min_mode_num
            min_mode_num = num

print(round(num_sum/N), num_median, min_mode_num if snd_mode_num > 4000 else snd_mode_num, num_max-num_min,sep='\n')