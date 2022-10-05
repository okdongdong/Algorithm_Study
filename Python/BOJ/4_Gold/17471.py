import sys
input = sys.stdin.readline


def check_area(_area: set) -> bool:
    area = set() | _area
    if not area:
        return False

    stack = [area.pop()]

    while stack:
        now_node = stack.pop()
        for next_node in network[now_node]:
            if next_node in area:
                stack.append(next_node)
                area.discard(next_node)

    return len(area) == 0


N = int(input())
populations = [0] + list(map(int, input().split()))
total_populations = sum(populations)
min_diff = 1001
network = [[] for _ in range(N+1)]

for i in range(N):
    cnt_and_areas = list(map(int, input().split()))
    network[i+1].extend(cnt_and_areas[1:])

for i in range(1 << (N+1)):
    area1 = set()
    area2 = set()
    for j in range(N):
        if i & (1 << j):
            area1.add(j+1)
        else:
            area2.add(j+1)

    if check_area(area1) and check_area(area2):
        area1_populations = sum(map(lambda x: populations[x], area1))
        diff = abs(area1_populations*2 - total_populations)
        min_diff = min(diff, min_diff)

print(min_diff if min_diff < 1001 else -1)
