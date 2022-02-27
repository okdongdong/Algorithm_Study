# 스타트와 링크.
import sys
input = sys.stdin.readline


def select(_cnt, _idx=0):   
    global min_val
    if _cnt == N//2:            # 절반을 뽑은 경우
        temp_val = 0            # 두팀의 능력치 차이를 저장할 임시변수
        for i in range(N):
            if check[i]:              # 두팀의 능력치 차이를 구해야하므로,
                temp_val += v_sum[i]  # A팀의 점수는 더하고
            else:
                temp_val -= h_sum[i]  # B팀의 점수는 빼줘서 차이를 구한다.
        if min_val > abs(temp_val):   # 두 팀의 능력치 차이가 최소인 경우
            min_val = abs(temp_val)
        return

    for i in range(_idx, N):    # 전체인원에서 A팀을 뽑음(조합)
        check[i] = True
        select(_cnt+1, i+1)     # 조합으로 뽑아야하므로, 현재까지 뽑은 인원 수와 인덱스를 넘겨줌
        check[i] = False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
v_sum = [0]*N
h_sum = [0]*N
check = [False]*N   # A팀은 True, B팀은 False로 지정

for r in range(N):
    for c in range(N):
        v_sum[c] += arr[r][c]   # A팀의 능력치 점수(세로합)
        h_sum[r] += arr[r][c]   # B팀의 능력치 점수(가로합)

min_val = 9876543210    # 최솟값을 구해야하므로 충분히 큰 값으로 지정
select(0)               # 재귀함수 실행
print(min_val)
