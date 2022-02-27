# 폴리오미노
board = input()
result = ''
cnt = 0
if board[0] == 'X':
    cnt = 1
else:
    result = '.'

for i in range(1, len(board)):
    if board[i] == 'X':
        cnt += 1
        if cnt < 4 and i < len(board)-1:
            continue

    if cnt == 4:
        result += 'AAAA'
    elif cnt == 2:
        result += 'BB'
    elif cnt != 0:
        result = ''
        break

    if (board[i] == '.' and board[i-1] == 'X') or cnt == 0:
        result += '.'

    cnt = 0

print(result if result else -1)
