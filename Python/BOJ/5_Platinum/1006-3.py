# 습격자 초라기

def cal_dp():
    # (1~N, 1~N) / (1~N, 1~N-1) / (1~N-1, 1~N)
    both_dp = [0] * N
    inner_dp = [0] * N
    outer_dp = [0] * N

    both_dp[0] = 1+int(inner_wontagon[0]+outer_wontagon[0] > W)
    inner_dp[0] = 1
    outer_dp[0] = 1

    # 안쪽 바깥쪽 모두 연결되지 않은 경우
    for i in range(1, N):
        inner_dp[i] = min(
            both_dp[i-1]+1,
            outer_dp[i-1]+1+int(inner_wontagon[i-1]+inner_wontagon[i] > W)
        )
        outer_dp[i] = min(
            both_dp[i-1]+1,
            inner_dp[i-1]+1+int(outer_wontagon[i-1]+outer_wontagon[i] > W)
        )
        both_dp[i] = min(
            both_dp[i-1]+1+int(inner_wontagon[i]+outer_wontagon[i] > W),
            inner_dp[i]+1,
            outer_dp[i]+1,
            both_dp[i-2]+2 if inner_wontagon[i-1] +
            inner_wontagon[i] <= W and outer_wontagon[i-1]+outer_wontagon[i] <= W else 99999999
        )

    return both_dp[-1]


T = int(input())

result = []
for _ in range(T):
    N, W = map(int, input().split())
    inner_wontagon = list(map(int, input().split()))
    outer_wontagon = list(map(int, input().split()))

    cnt = cal_dp()

    # 안쪽만 연결된 경우
    if N > 2 and inner_wontagon[0] + inner_wontagon[-1] <= W:
        temp = inner_wontagon[0], inner_wontagon[-1]
        inner_wontagon[0] = inner_wontagon[-1] = W+1
        cnt = min(cal_dp()-1, cnt)
        inner_wontagon[0], inner_wontagon[-1] = temp

    # 바깥쪽만 연결된 경우
    if N > 2 and outer_wontagon[0] + outer_wontagon[-1] <= W:
        temp = outer_wontagon[0], outer_wontagon[-1]
        outer_wontagon[0] = outer_wontagon[-1] = W+1
        cnt = min(cal_dp()-1, cnt)
        outer_wontagon[0], outer_wontagon[-1] = temp

        # 모두 연결된 경우
    if N > 2 and inner_wontagon[0] + inner_wontagon[-1] <= W and outer_wontagon[0] + outer_wontagon[-1] <= W:
        inner_wontagon[0] = inner_wontagon[-1] = W+1
        outer_wontagon[0] = outer_wontagon[-1] = W+1
        cnt = min(cal_dp()-2, cnt)

    result.append(cnt)

print(*result)
