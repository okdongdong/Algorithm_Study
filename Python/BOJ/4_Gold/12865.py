# 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
things_w_v = [list(map(int, input().split())) for _ in range(N)]
bag = [[0]*(K+1) for _ in range(N)]

for thing_num, (w, v) in enumerate(things_w_v):
    for weight in range(1, K+1):    # 남는 무게를 고려해야 하므로 무게 1~K까지 모두 순회
        # 현재물건을 무조건 넣는다고 했을 때, 현재물건의 가치 + 남은 무게에 넣을 수 있는 최대 가치 
        # vs 이전까지 계산된 현재무게에 넣을수 있는 최대 가치
        if weight >= w: 
            bag[thing_num][weight] = max(bag[thing_num-1][weight-w] + v, bag[thing_num-1][weight])
        else:
            bag[thing_num][weight] = bag[thing_num-1][weight]

print(bag[-1][-1])