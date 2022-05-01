# 동전 뒤집기

def flip_coin(n):
    global min_tail

    if n == N:
        now_tail = 0
        for r in range(N):
            temp_sum = sum(coin[r])
            now_tail += min(temp_sum, N-temp_sum)

        min_tail = min(min_tail, now_tail)
        return

    flip_coin(n+1)

    for r in range(N):
        coin[r][n] = 1-coin[r][n]

    flip_coin(n+1)
    for r in range(N):
        coin[r][n] = 1-coin[r][n]


N = int(input())
coin = [[0]*N for _ in range(N)]

for r in range(N):
    temp = input()
    for c in range(N):
        if temp[c] == 'T':
            coin[r][c] = 1

min_tail = N**2
flip_coin(0)
print(min_tail)
