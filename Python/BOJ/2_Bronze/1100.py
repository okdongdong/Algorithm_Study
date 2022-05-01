# 하얀 칸

chess = [input() for _ in range(8)]
cnt = 0
for r in range(8):
    for c in range(8):
        if (r+c) % 2:
            continue
        if chess[r][c] == 'F':
            cnt += 1
print(cnt)
