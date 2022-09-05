def cal_cnt(room):
    room_space = []
    for i in range(len(room)):
        room_space.extend(room[i])
    cnt = 0
    for r in room_space:
        if len(r) >= 2:
            cnt += 1
    return cnt


N = int(input())
room = [input() for _ in range(N)]
room1 = list(map(lambda x: x.split('X'), room))
room2 = list(map(lambda x: ''.join(x).split('X'), zip(*room)))

print(cal_cnt(room1), cal_cnt(room2))
