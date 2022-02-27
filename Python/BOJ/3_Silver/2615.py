def Omok():

    def direction(a, b):
        if omok_space[y][x]:
            try:
                if omok_space[y][x] != omok_space[y+5*b][x+5*a] and omok_space[y][x] != omok_space[y-b][x-a]:
                    for i in range(1, 5): 
                        if omok_space[y+i*b][x+i*a] != omok_space[y][x]:
                            break
                    else:
                        return f'{omok_space[y][x]}\n{y} {x}'
            except: pass
        return None

    x, y = 1, 1

    while y < 20:
        xy = [(1,0), (0,1), (1,1), (1,-1)] # 가로, 세로, 우하대각, 우상대각
        for a, b in xy:
            if direction(a,b):
                return direction(a,b)
        
        x += 1
        if x > 19:
            x = 1
            y += 1
    
    return 0

omok_space =[[0]*21] + [list(map(int, ['0'] + input().split() + ['0'])) for _ in range(19)] + [[0]*21] # 육목 검사시 인덱스에러 방지
print(Omok())










################

# def Omok():
#     x, y = 1, 1

#     while y < 20:
        
#         if omok_space[y][x]:
#             try:
#                 if omok_space[y][x] != omok_space[y][x+5] and omok_space[y][x] != omok_space[y][x-1]:  # 가로
#                     for i in range(1, 5): 
#                         if omok_space[y][x+i] != omok_space[y][x]:
#                             break
#                     else:
#                         return f'{omok_space[y][x]}\n{y} {x}'
#             except: pass
            
#             try:
#                 if omok_space[y][x] != omok_space[y+5][x] and omok_space[y][x] != omok_space[y-1][x]:  # 세로
#                     for i in range(1, 5): 
#                         if omok_space[y+i][x] != omok_space[y][x]:
#                             break
#                     else:
#                         return f'{omok_space[y][x]}\n{y} {x}'
#             except: pass
            
#             try:
#                 if omok_space[y][x] != omok_space[y+5][x+5] and omok_space[y][x] != omok_space[y-1][x-1]:  # 우하향대각
#                     for i in range(1, 5): 
#                         if omok_space[y+i][x+i] != omok_space[y][x]:
#                             break
#                     else:
#                         return f'{omok_space[y][x]}\n{y} {x}'
#             except: pass
            
#             try:            
#                 if y > 5:
#                     if omok_space[y][x] != omok_space[y-5][x+5] and omok_space[y][x] != omok_space[y+1][x-1]:  # 우상향대각
#                         for i in range(1, 5): 
#                             if omok_space[y-i][x+i] != omok_space[y][x]:
#                                 break
#                         else:
#                             return f'{omok_space[y][x]}\n{y} {x}'
#             except: pass

#         x += 1
#         if x > 19:
#             x = 1
#             y += 1
    
#     return 0


# omok_space =[[0]*21] + [list(map(int, ['0'] + input().split() + ['0'])) for _ in range(19)] + [[0]*21] # 육목 검사시 인덱스에러 방지
# print(Omok())