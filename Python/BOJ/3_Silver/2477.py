# 참외밭

K = int(input())
length_list = [[] for _ in range(4)]
order = [1, 3, 2, 4, 1] # 2개씩 있는 방향이 이 순서로 연속되게 있을때가 꺽이는 부분임
field = [list(map(int, input().split())) for _ in range(6)]

direction_cnt = [0]*4
direction_order = []
length_list = []

for direction, length in field:
    direction_cnt[direction-1] += 1
    length_list.append(length)
    direction_order.append(direction)

small = 0
big = 1
for i in range(6):
    if i < 5 and direction_cnt[direction_order[i]-1] == 2 and order[order.index(direction_order[i]) + 1] == direction_order[i+1]:
        small = length_list[i]*length_list[i+1]

    elif direction_cnt[direction_order[i]-1] == 1:
        big *= length_list[i]

if not small:
    direction_order.append(direction_order.pop(0))
    length_list.append(length_list.pop(0))
    for i in range(5):
        if direction_cnt[direction_order[i]-1] == 2 and order[order.index(direction_order[i]) + 1] == direction_order[i+1]:
            small = length_list[i]*length_list[i+1]

print((big - small)*K)
