# 경비원
import pprint

w, h = map(int, input().split())
N = int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
me = list(map(int, input().split()))

table = [[1] * (w + 1)] + [[1] + [0] * (w - 1) + [1] for _ in range(h - 1)] + [[1] * (w + 1)]
visited = [[0] * (w + 1) for _ in range(h + 1)]
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
stack = []
cnt, distance = 0, 0
for store in stores:
    if store[0] == 1:
        table[0][store[1]] = 2
    elif store[0] == 2:
        table[h][store[1]] = 2
    elif store[0] == 3:
        table[store[1]][0] = 2
    else:
        table[store[1]][w] = 2

if me[0] == 1:
    stack.append((0, me[1]))
elif me[0] == 2:
    stack.append((h, me[1]))
elif me[0] == 3:
    stack.append((me[1], 0))
else:
    stack.append((me[1], w))

while stack:
    temp = []
    cnt += 1
    for r, c in stack:
        for i in range(4):
            dr, dc = drc[i]
            nr = r + dr
            nc = c + dc
            if 0 <= nr <= h and 0 <= nc <= w and not visited[nr][nc]:
                if table[nr][nc]:
                    visited[nr][nc] = 1
                    temp.append((nr, nc))

                if table[nr][nc] == 2:
                    distance += cnt

    stack = temp

print(distance)
pprint.pprint(table)

# if me[0] == 1:

# elif me[0] == 2:
#     pass
# elif me[0] == 3:

# else:
#     h, w = w, -h


# for store in stores+[me]:
#     store[0] = (store[0]+4-me[0])%4
# print(stores, me)
# # me가 2인 경우를 기준으로    
# distance = 0
# for store in stores:
#     if store[0] == 0:
#         distance += abs(store[1]-me[1])
#     elif store[0] == 1:
#         distance += abs(h + me[1] - store[1] )
#     elif store[0] == 2:
#         distance += abs(w + store[1] - me[1])
#     else:
#         distance += min(abs(me[1] + store[1]+h),abs(2*w - (me[1] + store[1])+h))


# for store in stores+[me]:
#     if store[0] == 1:     store[0] = (0,-1)
#     elif store[0] == 2:   store[0] = (0,1)
#     elif store[0] == 3:   store[0] = (-1,0)
#     else:                 store[0] = (1,0)

# distance = 0

# for store in stores:
#     if me[0] == store[0]:             distance += abs(me[1] - store[1]) # 같은 변에 있을 때
#     elif me[0][0]+store[0][0] == 0:                                     # 반대쪽 변에 있을 때

#         if me[0][0]*store[0][0] == 0:                                   # 남북
#             distance += min(me[1] + store[1],2*w - (me[1] + store[1])) + h
#         else:                                                           # 동서
#             distance += min(me[1] + store[1],2*h - (me[1] + store[1])) + w

#     else:
#         if sum(me[0]+store[0])<0:     distance += me[1] + store[1]              # 서북
#         elif sum(me[0]+store[0])>0:   distance += h + w - (me[1] + store[1])    # 남동
#         else:
#             if me[0][0] == 1:         distance += w + store[1] - me[1]
#             elif store[0][0] == 1:    distance += w + me[1] - store[1] 
#             elif me[0][0] == -1:      distance += h + store[1] - me[1]
#             else:                     distance += h + me[1] - store[1] 

# print(distance)
