# 큐빙
def rotate(arr, reverse):
    result = [[0]*3 for _ in range(3)]
    if reverse:  # 시계방향
        for r in range(3):
            for c in range(3):
                result[2-c][r] = arr[r][c]

    else:       # 반시계방향
        for r in range(3):
            for c in range(3):
                result[c][2-r] = arr[r][c]

    return result


rotate_area = {
    0: [1, 3, 4, 2],
    1: [0, 2, 5, 3],
    2: [0, 4, 5, 1],
    3: [0, 1, 5, 4],
    4: [0, 3, 5, 2],
    5: [1, 2, 4, 3]
}   # 회전방향을 고려해서 생성(반시계방향)

direction_dict = {
    'U': 0, 'B': 1, 'L': 2, 'R': 3, 'F': 4, 'D': 5, '+': False, '-': True
}
result = ''
T = int(input())
for _ in range(T):
    N = int(input())
    cmd_list = input().split()
    cube = [
        [['w']*3 for _ in range(3)],
        [['o']*3 for _ in range(3)],
        [['g']*3 for _ in range(3)],
        [['b']*3 for _ in range(3)],
        [['r']*3 for _ in range(3)],
        [['y']*3 for _ in range(3)]
    ]

    for cmd in cmd_list:
        area = direction_dict[cmd[0]]
        rotation_direction = direction_dict[cmd[1]]
        cube[area] = rotate(cube[area], rotation_direction)
        if area == 0:
            if rotation_direction:  # 반시계방향
                temp = cube[rotate_area[area][0]][0]
                cube[rotate_area[area][0]][0] = cube[rotate_area[area][1]][0]
                cube[rotate_area[area][1]][0] = cube[rotate_area[area][2]][0]
                cube[rotate_area[area][2]][0] = cube[rotate_area[area][3]][0]
                cube[rotate_area[area][3]][0] = temp
            else:  # 시계방향
                temp = cube[rotate_area[area][3]][0]
                cube[rotate_area[area][3]][0] = cube[rotate_area[area][2]][0]
                cube[rotate_area[area][2]][0] = cube[rotate_area[area][1]][0]
                cube[rotate_area[area][1]][0] = cube[rotate_area[area][0]][0]
                cube[rotate_area[area][0]][0] = temp

        elif area == 5:
            if rotation_direction:  # 반시계방향
                temp = cube[rotate_area[area][0]][2]
                cube[rotate_area[area][0]][2] = cube[rotate_area[area][1]][2]
                cube[rotate_area[area][1]][2] = cube[rotate_area[area][2]][2]
                cube[rotate_area[area][2]][2] = cube[rotate_area[area][3]][2]
                cube[rotate_area[area][3]][2] = temp
            else:  # 시계방향
                temp = cube[rotate_area[area][3]][2]
                cube[rotate_area[area][3]][2] = cube[rotate_area[area][2]][2]
                cube[rotate_area[area][2]][2] = cube[rotate_area[area][1]][2]
                cube[rotate_area[area][1]][2] = cube[rotate_area[area][0]][2]
                cube[rotate_area[area][0]][2] = temp

        else:
            if area == 1:
                cube[0] = rotate(rotate(cube[0], False), False)
                cube[5] = rotate(rotate(cube[5], True), True)
            elif area == 2:
                cube[0] = rotate(cube[0], True)
                cube[5] = rotate(cube[5], False)
            elif area == 3:
                cube[0] = rotate(cube[0], False)
                cube[5] = rotate(cube[5], True)

            if rotation_direction:  # 반시계방향
                temp = []
                for r in range(3):
                    temp.append(cube[rotate_area[area][0]][2][2-r])
                for r in range(3):  # 위쪽
                    cube[rotate_area[area][0]
                         ][2][r] = cube[rotate_area[area][1]][r][0]
                for r in range(3):  # 오른쪽
                    cube[rotate_area[area][1]
                         ][r][0] = cube[rotate_area[area][2]][0][2-r]
                for r in range(3):  # 아래쪽
                    cube[rotate_area[area][2]
                         ][0][r] = cube[rotate_area[area][3]][r][2]
                for r in range(3):  # 왼쪽
                    cube[rotate_area[area][3]][r][2] = temp[r]

            else:                   # 반시계 방향
                temp = []
                for r in range(3):
                    temp.append(cube[rotate_area[area][3]][2-r][2])
                for r in range(3):  # 왼쪽
                    cube[rotate_area[area][3]
                         ][r][2] = cube[rotate_area[area][2]][0][r]
                for r in range(3):  # 아래쪽
                    cube[rotate_area[area][2]
                         ][0][r] = cube[rotate_area[area][1]][2-r][0]
                for r in range(3):  # 오른쪽
                    cube[rotate_area[area][1]
                         ][r][0] = cube[rotate_area[area][0]][2][r]
                for r in range(3):  # 위쪽
                    cube[rotate_area[area][0]][2][r] = temp[r]
            if area == 1:
                cube[0] = rotate(rotate(cube[0], True), True)
                cube[5] = rotate(rotate(cube[5], False), False)
            elif area == 2:
                cube[0] = rotate(cube[0], False)
                cube[5] = rotate(cube[5], True)
            elif area == 3:
                cube[0] = rotate(cube[0], True)
                cube[5] = rotate(cube[5], False)

    for temp in cube[0]:
        result += ''.join(temp) + '\n'

print(result.rstrip())
