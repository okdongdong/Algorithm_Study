# 타일 채우기
T = int(input())

# 초기상태 저장
dp = [1, 1, 5]
cnt = [0, 1, 4]

for _ in range(T):
    N = int(input())

    # 이미 계산해둔 값이면 바로 출력하고 넘어감
    if N < len(dp):
        print(dp[N])
        continue

    idx = len(dp)

    # 계산해둔 범위를 넘을 경우 계산해 줌
    while N >= idx:
        cnt.append(2 if idx % 2 else 3)
        temp = 0

        for i in range(idx):
            temp += dp[i] * cnt[-i-1]

        dp.append(temp)
        idx += 1

    # 계산한 값 출력
    print(dp[N])
