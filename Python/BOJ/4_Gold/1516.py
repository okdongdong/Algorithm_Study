N = int(input())
prev_buildings = [[] for _ in range(N + 1)]
times = [0] * (N + 1)

for building in range(1, N + 1):
    building_info = list(map(int, input().split()))
    times[building] = building_info[0]

    for prev_building in building_info[1:-1]:
        prev_buildings[building].append(prev_building)

dp = [0] * (N + 1)

oreder_list = []
buildings = set(range(1, N + 1))
visited = set()
while len(oreder_list) < N:

    for building in buildings:
        for prev_building in prev_buildings[building]:
            if prev_building not in visited:
                break
        else:
            oreder_list.append(building)
            visited.add(building)

    buildings -= visited

for building in oreder_list:
    edge = prev_buildings[building]
    if not edge:
        dp[building] = times[building]

    for prev_building in edge:
        dp[building] = max(dp[building], dp[prev_building] + times[building])

print(*dp[1:], sep="\n")
