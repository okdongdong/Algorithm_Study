# 두 가중치
import heapq

N = int(input())
weight1_list = [input() for _ in range(N)]
weight2_list = [input() for _ in range(N)]

edges = [[] for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if weight1_list[i][j] != '.':
            weight1 = int(weight1_list[i][j])
            weight2 = int(weight2_list[i][j])
            edges[i].append([weight1, weight2, j])
            edges[j].append([weight1, weight2, i])

cumulative_weight = [987654321]*N  # 0~특정노드까지 가중치 누적합
cumulative_weight[0] = 0
stack = [(0, 0, 0)]  # weight1, weight2, node

visited = [[False]*N for _ in range(N)]

while stack:
    now_weight1, now_weight2, now_node = heapq.heappop(stack)
    
    for next_weight1, next_weight2, next_node in edges[now_node]:
        if next_node == 0:
            continue

        if cumulative_weight[next_node] > (now_weight1+next_weight1)*(now_weight2+next_weight2):
            cumulative_weight[next_node] = (now_weight1+next_weight1)*(now_weight2+next_weight2)
            heapq.heappush(stack, (now_weight1+next_weight1, now_weight2+next_weight2, next_node))

        elif next_node != 1 and not visited[now_node][next_node]:
            heapq.heappush(stack, (now_weight1+next_weight1, now_weight2+next_weight2, next_node))

        visited[now_node][next_node] = True
        
print(-1 if cumulative_weight[1] == 987654321 else cumulative_weight[1])
