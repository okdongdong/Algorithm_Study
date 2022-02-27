# 남극 탐험
from time import time
import sys
input = sys.stdin.readline

##
N = int(input())
penguins = [0] + list(map(int, input().split()))
penguins_cnt = dict()
Q = int(input())
cmd_list = [input().split() for _ in range(Q)]
bridges = dict()
flag = True

s = time()

for i in range(1, N+1):
    bridges[(i,i)] = set([i])
result = []

for idx in range(Q):
    cmd, A, B = cmd_list[idx]
    A = int(A)
    B = int(B)
    if A > B:
        A, B = B, A

    if cmd == 'bridge':
        if bridges.get((A, B)):
            result.append('no')
        else:
            bridges[(A, B)]=set([A,B])

            for i in range(1, N+1):
                if A==i or B==i:
                        continue
                if B < i :
                    
                    if bridges.get((A, i)) and not bridges.get((B, i)):
                        bridges[(B, i)]=bridges[(A, i)]|bridges[(A, B)]

                    if bridges.get((B, i)) and not bridges.get((A, i)):
                        bridges[(A, i)]=bridges[(B, i)]|bridges[(A, B)]

                elif i < A:

                    if bridges.get((i, A)) and not bridges.get((i, B)):
                        bridges[(i, B)]=bridges[(i, A)]|bridges[(A, B)]

                    if bridges.get((i, B)) and not bridges.get((i, A)):
                        bridges[(i, A)]=bridges[(i, B)]|bridges[(A, B)]

                else:

                    if bridges.get((A, i)) and not bridges.get((B, i)):
                        bridges[(B, i)]=bridges[(A, i)]|bridges[(A, B)]
                        
                    if bridges.get((i, B)) and not bridges.get((i, A)):
                        bridges[(i, A)]=bridges[(i, B)]|bridges[(A, B)]
            
            result.append('yes')

    elif cmd == 'penguins':
        penguins[A] = B
        flag = False
        
    elif cmd == 'excursion':
        if flag and penguins_cnt.get((A, B)):
            result.append(penguins_cnt.get((A, B)))
        else:
            for i in range(1, N+1):
                if bridges.get((A, B)):
                    break
                if A==i or B==i:
                    continue

                if B < i :
                    if bridges.get((A, i)) and bridges.get((B, i)):
                        bridges[(A, B)]=bridges[(A, i)]|bridges[(B, i)]
                    
                elif i < A:
                    if bridges.get((i, A)) and bridges.get((i, B)):
                        bridges[(A, B)]=bridges[(i, A)]|bridges[(i, B)]

                else:
                    if bridges.get((A, i)) and bridges.get((i, B)):
                        bridges[(A, B)]=bridges[(A, i)]|bridges[(i, B)]

            if bridges.get((A, B)):
                cnt = 0
                for i in bridges.get((A, B)):
                    cnt += penguins[i]
                penguins_cnt[(A, B)] = cnt
                result.append(cnt)
            else:
                result.append('impossible')

print(*result, sep='\n')

e = time()

print(e-s)

# import sys
# input = sys.stdin.readline

# ##
# N = int(input())
# penguins = [0] + list(map(int, input().split()))
# Q = int(input())
# cmd_list = [input().split() for _ in range(Q)]
# bridges = [[set() for _ in range(N+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     bridges[i][i].add(i)
# result = []

# for cmd, A, B in cmd_list:
#     A = int(A)
#     B = int(B)

#     if cmd == 'bridge':
#         visited = [False]*(N+1)
#         if bridges[A][B]:
#             result.append('no')
#         else:
#             bridges[A][B].update([A,B])
#             bridges[B][A].update([A,B])

#             for i in range(1, N+1):
#                 if A==i or B==i:
#                         continue
                    
#                 if bridges[A][i] and not bridges[B][i]:
#                     bridges[B][i].update(bridges[A][i],bridges[A][B])
#                     bridges[i][B].update(bridges[i][A],bridges[B][A])

#                 if bridges[B][i] and not bridges[A][i]:
#                     bridges[A][i].update(bridges[B][i],bridges[A][B])
#                     bridges[i][A].update(bridges[i][B],bridges[B][A])
            
#             result.append('yes')

#     elif cmd == 'penguins':
#         penguins[A] = B
        
#     elif cmd == 'excursion':
#         for i in range(1, N+1):
#             if bridges[A][B]:
#                 break
#             if A==i or B==i:
#                 continue
#             if bridges[A][i] and bridges[B][i]:
#                 bridges[A][B].update(bridges[A][i],bridges[B][i])
#                 bridges[B][A].update(bridges[i][A],bridges[i][B])

#         if bridges[A][B]:
#             cnt = 0
#             for i in bridges[A][B]:
#                 cnt += penguins[i]
#             result.append(cnt)
#         else:
#             result.append('impossible')

# print(*result, sep='\n')

############################

# import sys
# from pprint import pprint
# input = sys.stdin.readline

# ##
# N = int(input())
# penguins = [0] + list(map(int, input().split()))
# Q = int(input())
# cmd_list = [input().split() for _ in range(Q)]
# bridges = [[[] for _ in range(N+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     bridges[i][i].append(i)
# result = []

# for cmd, A, B in cmd_list:
#     A = int(A)
#     B = int(B)

#     if cmd == 'bridge':
#         visited = [False]*(N+1)
#         if bridges[A][B]:
#             result.append('no')
#         else:
#             pprint(bridges)
#             bridges[A][B] += [A,B]
#             bridges[B][A] += [A,B]
            
#             for i in range(1, N+1):
#                 if A==i or B==i:
#                         continue
                
#                 if bridges[A][i] and not bridges[B][i]:
#                     bridges[B][i] = bridges[A][i] + [B]
#                     bridges[i][B] = bridges[i][A] + [B]

#                 if bridges[B][i] and not bridges[A][i]:
#                     bridges[A][i] = bridges[B][i] + [A]
#                     bridges[i][A] = bridges[i][B] + [A]

#             result.append('yes')

#     elif cmd == 'penguins':
#         penguins[A] = B
        
#     elif cmd == 'excursion':
#         island_route = [A]
#         visited = [False]*(N+1)
#         print(bridges[A][B])
#         if bridges[A][B]:
#             cnt = 0
#             for i in bridges[A][B]:
#                 cnt += penguins[i]
#             result.append(cnt)
#         else:
#             result.append('impossible')

# pprint(bridges)
# print(*result, sep='\n')



#################

# import sys
# sys.setrecursionlimit(30000)
# input = sys.stdin.readline

# def move(A, B, temp_route):
#     global island_route
#     visited[A] = True
#     if A == B:
#         island_route += temp_route
#         return True
#     for i in bridges[A]:
#         if visited[i]:
#             continue
#         temp_route.append(i)
        
#         if move(i, B, temp_route):
#             break

#         temp_route.pop()
#     else:
#         return False
#     return True 

# def is_move_possible(A, B):
#     visited = [False]*(N+1)
#     stack = [A]

#     while stack:
#         next_island = stack.pop()

#         if next_island == B:
#             return True
        
#         if visited[next_island]:
#             continue

#         visited[next_island] = True

#         for i in bridges[next_island]:
#             stack.append(i)    
        
#     return None

# ##
# N = int(input())
# penguins = [0] + list(map(int, input().split()))
# Q = int(input())
# cmd_list = [input().split() for _ in range(Q)]
# bridges = [[] for _ in range(N+1)]
# island_visited = [False]*(N+1)
# result = []

# for cmd, A, B in cmd_list:
#     A = int(A)
#     B = int(B)

#     if cmd == 'bridge':
#         visited = [False]*(N+1)
#         if is_move_possible(A, B):
#             result.append('no')
#         else:
#             bridges[A].append(B)
#             bridges[B].append(A)
#             result.append('yes')

#     elif cmd == 'penguins':
#         penguins[A] = B
        
#     elif cmd == 'excursion':
#         island_route = [A]
#         visited = [False]*(N+1)
#         if move(A, B, []):
#             cnt = 0
#             for i in island_route:
#                 cnt += penguins[i]
#             result.append(cnt)
#         else:
#             result.append('impossible')

# print(*result, sep='\n')