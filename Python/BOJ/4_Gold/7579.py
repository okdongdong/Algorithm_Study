# 앱
N, M = map(int, input().split())
memorys = list(map(int, input().split()))
costs = list(map(int, input().split()))

# 메모리의 최대값이 매우 크므로 비용을 기준으로 dp

max_memory = [0]*10001  # ∑c <= 10000

for i in range(N):
    for cost in range(10000, -1, -1):
        if cost >= costs[i]:
            max_memory[cost] = max(max_memory[cost-costs[i]] + memorys[i], max_memory[cost])
        
for cost, memory in enumerate(max_memory):
    if memory >= M:
        print(cost)
        break
