# 최소비용 구하기 2
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
bus_route = [dict() for _ in range(N+1)]
cost_list = [([], 987654321) for _ in range(N+1)]
for _ in range(M):
    s, e, cost = map(int, input().split())
    if bus_route[s].get(e) and bus_route[s][e] <= cost:
        continue

    bus_route[s][e] = cost

start, end = map(int, input().split())
cost_list[start] = ([start], 0)

stack = [start]
while stack:
    now_city = stack.pop()
    if now_city == end:
        continue

    for next_city, next_cost in bus_route[now_city].items():
        if cost_list[end][1] <= cost_list[now_city][1] + next_cost:
            continue

        if cost_list[next_city][1] > cost_list[now_city][1] + next_cost:
            cost_list[next_city] = (
                cost_list[now_city][0] + [next_city], cost_list[now_city][1] + next_cost)
            stack.append(next_city)

print(cost_list[end][1])
print(len(cost_list[end][0]))
print(*cost_list[end][0])
