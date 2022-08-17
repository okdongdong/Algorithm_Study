N = int(input())
positions = map(int, input().split())
order = sorted(set(positions))
position_dict = {}

for idx, x in enumerate(order):
    position_dict[x] = idx

result = []
for x in positions:
    result.append(position_dict[x])

print(*result)
