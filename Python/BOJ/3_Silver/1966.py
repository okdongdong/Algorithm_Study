# 프린터 큐
from collections import deque

T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    paper_priority = list(map(int, input().split()))
    paper_priority_list = deque(paper_priority)
    order = 0
    M_priority = paper_priority_list[M]
    paper_priority_list[M] = -1
    
    now_priority = 9
    while now_priority >= M_priority:
        cnt = paper_priority.count(now_priority)
        while cnt > 0:
            temp = paper_priority_list.popleft()
            if now_priority==M_priority and temp == -1:
                order += 1
                break

            if temp == now_priority:
                order += 1
                cnt -= 1
                continue
            paper_priority_list.append(temp)
        now_priority -= 1
    result.append(order)

print(*result, sep='\n')

# T = int(input())
# result = []
# for _ in range(T):
#     N, M = map(int, input().split())
#     paper_priority_list = list(map(int, input().split()))
#     order = 0
#     M_priority = paper_priority_list[M]
#     now_idx = M
#     for now_priority in range(9, M_priority, -1):
#         for idx, paper_priority in enumerate(paper_priority_list):
#             if paper_priority == now_priority:
#                 order += 1
#                 now_idx = idx

#     if now_idx > M:
#         for i in range(now_idx, N):
#             if paper_priority_list[i] == M_priority:
#                 order += 1
    
#     for i in range(M+1):
#         if paper_priority_list[i] == M_priority:
#                 order += 1
    
#     result.append(order)

# print(*result, sep='\n')
