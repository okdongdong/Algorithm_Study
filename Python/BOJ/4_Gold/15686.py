# 치킨 배달
def cal_distance():
    distance_list = [987654]*len(house)
    for i in range(len(chicken_house)):
        if chicken_check[i]:
            continue
        ch_r, ch_c = chicken_house[i]
        for j in range(len(house)):
            h_r, h_c = house[j]
            distance_list[j] = min(distance_list[j], abs(ch_r - h_r)+abs(ch_c - h_c))

    return sum(distance_list)


def min_chicken_distance(_cnt=0, _start_idx=0):
    global min_distance

    if _cnt == len(chicken_house) - M:
        _distance = cal_distance()
        if min_distance > _distance:
            min_distance = _distance
        return

    for i in range(_start_idx, len(chicken_house)):
        if chicken_check[i]:
            continue

        chicken_check[i] = True

        min_chicken_distance(_cnt+1, i+1)

        chicken_check[i] = False


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
min_distance = 9876543210
chicken_house = []
house = []

# 치킨집 찾기
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house.append((r, c))
        elif city[r][c] == 2:
            chicken_house.append((r, c))

chicken_check = [False]*len(chicken_house)

min_chicken_distance()

print(min_distance)