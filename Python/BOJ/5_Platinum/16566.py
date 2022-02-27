# # 카드 게임

# N, M, K = map(int, input().split())
# cards = list(map(int, input().split()))
# cards.sort()

# inhand = list(map(int, input().split()))
 
# for card in inhand:
#     # 이분탐색
#     card 


    # 낚시왕

direction_mapping = {
    1: 0, 2: 2, 3: 1, 4: 3
}
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

height, width, N = map(int, input().split())

board = [[""] * width for _ in range(height)]

shark = {}

for _ in range(1, N + 1):
    r, c, s, d, z = map(int, input().split())

    board[r - 1][c - 1] += str(_)
    shark[_] = [r - 1, c - 1, s, direction_mapping[d], z]
result = 0
for pos in range(width):
    for r in range(height):
        if board[r][pos]:
            result += shark[int(board[r][pos])][4]
            shark[int(board[r][pos])] = 0
            break

    board = [[""] * width for _ in range(height)]
    for i in range(1, N + 1):
        if shark[i] != 0:
            r, c, s, d, z = shark[i]
            dis = s
            while True:
                if 0 <= r + dis * dr[d] < height and 0 <= c + dis * dc[d] < width:
                    r += dis * dr[d]
                    c += dis * dc[d]
                    break
                else:
                    if dr[d]:
                        dis -= abs(r - (0 if dr[d] == -1 else (height - 1)))
                        r = 0 if dr[d] == -1 else (height - 1)
                    else:
                        dis -= abs(c - (0 if dc[d] == -1 else (width - 1)))
                        c = 0 if dc[d] == -1 else (width - 1)
                    d = (d + 2) % 4
            shark[i] = [r, c, s, d, z]
            board[r][c] += str(i)

    for i in range(height):
        for j in range(width):
            if len(board[i][j]) > 1:
                max_size = 0
                max_idx = 0
                for idx in board[i][j]:
                    if shark[int(idx)][4] > max_size:
                        max_idx = idx
                        max_size = shark[int(idx)][4]

                for idx in board[i][j]:
                    if idx != max_idx:
                        shark[int(idx)] = 0

                board[i][j] = max_idx

print(result)