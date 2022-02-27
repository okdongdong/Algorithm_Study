# 퇴사
def counseling(day, profit):  # day와 이익을 인자로 넘겨줌
    global max_profit
    if profit > max_profit:  # 이익의 최댓값 갱신
        max_profit = profit

    if day > N - 1:  # 퇴사일 이후가 되면 상담불가
        return

    T, P = TP_list[day]
    if check[day] or day + T > N:
        counseling(day + 1, profit)  # 이전 상담일정과 겹치는 경우 다음날로 이동
    else:
        for i in range(day, day + T):
            check[i] = True
        counseling(day + 1, profit + P)  # day에서 상담을 진행한 경우
        for i in range(day, day + T):
            check[i] = False
        counseling(day + 1, profit)  # day에서 상담을 진행하지 않고 다음날로 이동하는 경우


N = int(input())
TP_list = [list(map(int, input().split())) for _ in range(N)]
max_profit = 0
check = [False] * N
counseling(0, 0)  # 재귀 활용한 완전탐색
print(max_profit)
