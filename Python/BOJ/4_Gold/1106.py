C, N = map(int, input().split())
INF = float("inf")
costs = [INF] * 1001
costs[0] = 0
invests = []

for _ in range(N):
    a, b = map(int, input().split())
    costs[b] = min(a, costs[b])
    invests.append((a, b))

for a, b in invests:
    for i in range(C + 1):
        j = min(i + b, C)
        costs[j] = min(costs[j], costs[i] + a)

print(costs[C])
