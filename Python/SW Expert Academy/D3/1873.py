# 1873. 상호의 배틀필드
def findme():
    for r in range(H):
        for c in range(W):
            for i in range(4):
                if field[r][c] == direction_list[i]:
                    return (r, c, direction_list[i])

# 상하좌우
cmd_dir_list = ['U', 'D', 'L', 'R']
drc_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_list = ['^', 'v', '<', '>']

T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    cmd_list = input()
    me_r, me_c, me = findme()

    for cmd in cmd_list:
        if cmd == 'S':  # 포탄 발사
            bomb_idx = direction_list.index(me)
            b_r, b_c = drc_list[bomb_idx]
            bomb_r, bomb_c = me_r, me_c

            while 0 <= bomb_r < H and 0 <= bomb_c < W:
                if field[bomb_r][bomb_c] == '#':
                    break

                if field[bomb_r][bomb_c] == '*':
                    field[bomb_r][bomb_c] = '.'
                    break

                bomb_r += b_r
                bomb_c += b_c

        else:   # move
            me_idx = cmd_dir_list.index(cmd)
            r, c = drc_list[me_idx]
            me = direction_list[me_idx]

            if 0 <= me_r + r < H and 0 <= me_c + c < W and field[me_r + r][me_c + c] == '.':
                field[me_r][me_c] = '.'
                me_r += r
                me_c += c

            field[me_r][me_c] = me

    print('#', tc, sep='', end=' ')
    for f in field:
        print(*f, sep='')
