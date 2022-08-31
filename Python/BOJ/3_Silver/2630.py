# 색종이 만들기

def check(n, sr, sc):
    now_color = board[sr][sc]

    if n == 1:
        colors[now_color] += 1
        return

    for r in range(sr, sr+n):
        for c in range(sc, sc+n):
            if board[r][c] != now_color:
                nn = n//2
                check(nn, sr, sc)
                check(nn, sr+nn, sc)
                check(nn, sr, sc+nn)
                check(nn, sr+nn, sc+nn)
                return

    colors[now_color] += 1


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
colors = [0, 0]
check(N, 0, 0)
print(*colors, sep='\n')
