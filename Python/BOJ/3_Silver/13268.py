# 셔틀런

def shuttle_run(corn):
    temp = corn + corn[-2::-1]  # 콘이 있는 지점을 한번만 포함하도록 리스트 구성
    ans = []
    for lst in temp:
        ans.append((lst - 1) // 5 + 1)  # 구간별 숫자로 변환
    return ans


N = int(input())
n = N % 100
corn0 = [0]                 # 시작점
corn1 = list(range(1, 6))   # 각 콘별 포함하는 구간을 리스트로 표현
corn2 = list(range(1, 11))
corn3 = list(range(1, 16))
corn4 = list(range(1, 21))
corns = [corn1, corn2, corn3, corn4]

result_lst = []
for c in corns:
    result_lst += corn0 + shuttle_run(c)
    # 매 왕복마다 시작점을 찍으므로 추가해줌, 출발점은 구간 숫자가 0이므로 따로 계산했음
print(result_lst[n])
