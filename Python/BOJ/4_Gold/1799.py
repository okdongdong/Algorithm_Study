# 비숍 

def chess(start=0, cnt=0):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt

    for i in range(start, len(check)):
        if len(check) - start < max_cnt - cnt:
            return

        r, c = check[i]
        if visited[r][c]:
            continue

        visited[r][c] = True
        for dr, dc in drc:
            for n in range(1,N):
                nr = r+dr*n
                nc = c+dc*n
                if not (0<=nr<N and 0<=nc<N):
                    break
                visited[nr][nc] = True

        chess(start+1, cnt+1)
        
        visited[r][c] = False
        for dr, dc in drc:
            for n in range(1,N):
                nr = r+dr*n
                nc = c+dc*n
                if not (0<=nr<N and 0<=nc<N):
                    break
                visited[nr][nc] = False




drc = [(1,1),(-1,1),(1,-1),(-1,-1)]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
check = []
max_cnt =0

for r in range(N):
    for c in range(N):
        if board[r][c]:
            check.append((r,c))

chess()

print(max_cnt)