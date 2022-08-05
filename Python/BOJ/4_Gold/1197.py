# 최소 스패닝 트리
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

V, E = map(int, input().split())

edges = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    edges[s].append((e, w))
    edges[e].append((s, w))

que = [(0, 1)]  # w, s
visited = [False]*(V+1)
min_weight = 0

while que:
    w, s = heappop(que)
    if visited[s]:
        continue

    min_weight += w
    visited[s] = True

    for e, next_w in edges[s]:
        heappush(que, (next_w, e))

print(min_weight)


# edges = [list(map(int, input().split())) for _ in range(E)]
# edges.sort(key=lambda x: x[2])
# visited_list = [{edges[0][0], edges[0][1]}]
# result = edges[0][2]
# for edge in edges:
#     v1, v2, value = edge
#     check_idx = -1
#     flag = True
#     for idx in range(len(visited_list)):
#         # print(visited_list)
#         if (v1 in visited_list[idx]) and (v2 in visited_list[idx]):
#             flag = False
#             break
#         elif (v1 in visited_list[idx]) or (v2 in visited_list[idx]):
#             visited_list[idx].add(v1)
#             visited_list[idx].add(v2)

#             if check_idx < 0:
#                 result += value
#                 check_idx = idx
#                 flag = False
#             else:
#                 visited_list[check_idx] = visited_list[check_idx] | visited_list[idx]
#                 visited_list.pop(idx)
#                 break
#     else:
#         if flag:
#             visited_list.append({v1, v2})
#             result += value

# # print(visited_list)
# print(result)
