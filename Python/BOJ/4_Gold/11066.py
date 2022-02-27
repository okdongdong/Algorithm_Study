# 파일 합치기
import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    K = int(input())
    page_cost = list(map(int, input().split()))

    # arr[합쳐진 파일 수1][시작하는 파일 번호] = (현재파일을 만드는 데 필요한 비용, 현재까지 누적합)
    cost_sum_list = [[(987654321, 987654321)]*K for _ in range(K+1)]

    # 한개짜리들의 비용을 넣어줌
    for i in range(K):
        cost_sum_list[1][i] = (page_cost[i], 0)

    for file_cnt in range(2, K+1):                      # 합쳐지는 파일 개수
        for start_file_num in range(K-file_cnt+1):      # 파일번호는 0번부터 시작
            for left_cnt in range(1, file_cnt):         # 분할되는 방법(나눠지는 개수)
                right_cnt = file_cnt - left_cnt
                left_cost, left_total = cost_sum_list[left_cnt][start_file_num]
                right_cost, right_total = cost_sum_list[right_cnt][start_file_num+left_cnt]
                now_cost = left_cost + right_cost
                now_total = left_total + right_total + now_cost
                if cost_sum_list[file_cnt][start_file_num][1] > now_total:
                    cost_sum_list[file_cnt][start_file_num] = (now_cost, now_total)
    
    result.append(str(cost_sum_list[K][0][1]))

print('\n'.join(result))