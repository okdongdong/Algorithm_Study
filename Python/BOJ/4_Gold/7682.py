# 틱택토

case_list = [  # 가로
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),

    # 세로
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),

    # 대각선
    (0, 4, 8),
    (2, 4, 6)]

result = []
while True:
    tictactoe = input()
    if tictactoe == 'end':
        break
    o_cnt = 0
    x_cnt = 0
    o_flag = False
    x_flag = False
    blank_flag = False
    for i in range(9):
        tic = tictactoe[i]
        if tic == 'O':
            o_cnt += 1
        elif tic == 'X':
            x_cnt += 1
        else:
            blank_flag = True

    # O가 먼저놓거나 X가 두번 놓는 경우
    if not (0 <= x_cnt - o_cnt < 2):
        result.append('invalid')
        continue

    for case in case_list:
        temp = ''
        for i in case:
            if tictactoe[i] == '.':
                break

            if not temp:
                temp = tictactoe[i]
                continue

            if tictactoe[i] != temp:
                break

        else:
            if temp == 'O':
                o_flag = True
            else:
                x_flag = True

    # OX가 동시에 완성되어있는 경우나 OX가 완성된 이후 XO가 놓여진 경우
    if (o_flag or x_cnt <= o_cnt) and (x_flag or x_cnt > o_cnt):
        result.append('invalid')
        continue

    # 아무것도 완성되지 않고 가득차지도 않았을 때
    if not o_flag and not x_flag and blank_flag:
        result.append('invalid')
        continue

    result.append('valid')

print('\n'.join(result))


