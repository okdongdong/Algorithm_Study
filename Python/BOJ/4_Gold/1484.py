G = int(input())
result = []

for prev_weight in range(1, G):
    now_weight = (prev_weight**2 + G) ** 0.5
    if now_weight == int(now_weight):
        result.append(int(now_weight))

print(*result if result else [-1], sep="\n")
