# 11315. 오목 판정

def isomok(r, c, d, cnt=1): 
    if arr[r][c] == 'o':
        if cnt == 5:
            return True
        dr, dc = d
        nr = r+dr
        nc = c+dc

        if 0 <= nr < N and 0 <= nc < N:
            if isomok(nr, nc, d, cnt+1):
                return True
        
    return False
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    direction = [(1,0),(0,1),(1,1),(-1,1)]  # 세로, 가로, 우하향, 우상향
    cnt = 1
    result = False
    for r in range(N):
        for c in range(N):
            for d in direction:
                if isomok(r,c,d):
                    result = True
                    break
            if result:
                break
        if result:
            break
    if result:
        print('#{} YES'.format(tc))        
    else: print('#{} NO'.format(tc))        
