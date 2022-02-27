# 청소년 상어
from copy import deepcopy


def fish_move(_shark_location, _shark_direction):
    global fish_locations, new_fish_arr, new_fish_dirs
    temp_fish_locations = deepcopy(fish_locations)
    temp_fish_dirs = deepcopy(new_fish_dirs)
    temp_fish_arr = deepcopy(new_fish_arr)
    for i in range(1, 17):
        if fish_locations[i] == 0:
            continue
        r, c = fish_locations[i]
        for _ in range(8):

            dr, dc = directions[new_fish_dirs[r][c]]

            if (0 <= r+dr < 4 and 0 <= c+dc < 4) and (r+dr, c+dc) != _shark_location:
                new_fish_arr[r][c], new_fish_arr[r+dr][c + dc] = new_fish_arr[r+dr][c+dc], new_fish_arr[r][c]
                new_fish_dirs[r][c], new_fish_dirs[r+dr][c + dc] = new_fish_dirs[r+dr][c+dc], new_fish_dirs[r][c]
                fish_locations[i] = (r+dr, c+dc)
                if fish_locations[new_fish_arr[r][c]]:
                    fish_locations[new_fish_arr[r][c]] = (r, c)
                break
            else:
                new_fish_dirs[r][c] = (new_fish_dirs[r][c]+1) % 8
                continue

    shark_move(_shark_location, _shark_direction)

    fish_locations = temp_fish_locations
    new_fish_dirs = temp_fish_dirs
    new_fish_arr = temp_fish_arr


def shark_move(_shark_location, _shark_direction):
    global max_num_sum
    r, c = _shark_location
    dr, dc = directions[_shark_direction]
    flag = True
    for i in range(1, 4):
        nr = r+dr*i
        nc = c+dc*i
        if 0 <= nr < 4 and 0 <= nc < 4:
            if new_fish_arr[nr][nc]:
                flag = False
                target_fish = new_fish_arr[nr][nc]
                fish_locations[target_fish] = 0
                new_fish_arr[nr][nc] = 0
                new_shark_direction = new_fish_dirs[nr][nc]
                new_shark_location = (nr, nc)

                fish_move(new_shark_location, new_shark_direction)

                new_fish_arr[nr][nc] = target_fish
                fish_locations[target_fish] = (nr, nc)

    if flag:
        now_num_sum = 136 - sum(map(sum, new_fish_arr))
        if now_num_sum > max_num_sum:
            max_num_sum = now_num_sum
        return


fish_arr = [list(map(int, input().split())) for _ in range(4)]
new_fish_arr = [[0]*4 for _ in range(4)]
new_fish_dirs = [[0]*4 for _ in range(4)]
directions = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]

fish_locations = [0]*17
max_num_sum = 0

for r in range(4):
    for c in range(0, 8, 2):
        fish_locations[fish_arr[r][c]] = [r, c//2]
        new_fish_arr[r][c//2] = fish_arr[r][c]
        new_fish_dirs[r][c//2] = (fish_arr[r][c+1]) % 8

shark_location = (0, 0)
shark_direction = new_fish_dirs[0][0]
fish_locations[new_fish_arr[0][0]] = 0
new_fish_arr[0][0] = 0

fish_move(shark_location, shark_direction)

print(max_num_sum)
