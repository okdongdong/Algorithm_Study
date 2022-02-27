N, M = map(int, input().split())
maze = [input() for _ in range(N)]

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

stack = [(0, 0)]
visited = [[0]*M for _ in range(N)]
cnt = 1

while True:     # 모든 경로에 대해 검사
    cnt += 1
    temp_stack = []
    
    for now_r, now_c in stack:
        for i in range(4):
            r = now_r + dr[i]
            c = now_c + dc[i]
            if not (0 <= r < N and 0 <= c < M):
                    continue
            
            if maze[r][c] == '1' and not visited[r][c]:
                temp_stack.append((r, c))
                visited[r][c] = 1
    
    stack = temp_stack

    if  (N-1, M-1) in stack:
        break

print(cnt)
