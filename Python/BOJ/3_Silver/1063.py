# 킹
import sys
input = sys.stdin.readline

move = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1),
}

king, stone, N = input().split()
cmd_list = [input().rstrip() for _ in range(int(N))]
king = list(king)
king[1] = int(king[1])
stone = list(stone)
stone[1] = int(stone[1])

for now_move in cmd_list:
    dr, dc = move[now_move]
    if not (0 < king[1] + dr <= 8 and 'A' <= chr(ord(king[0]) + dc) <= 'H'):
        continue

    king[0] = chr(ord(king[0]) + dc)
    king[1] = king[1] + dr

    if king == stone:
        if 0 < stone[1] + dr <= 8 and 'A' <= chr(ord(stone[0]) + dc) <= 'H':
            stone[0] = chr(ord(stone[0]) + dc)
            stone[1] = stone[1] + dr
        else:
            king[0] = chr(ord(king[0]) - dc)
            king[1] = king[1] - dr

print(*king, sep='')
print(*stone, sep='')
