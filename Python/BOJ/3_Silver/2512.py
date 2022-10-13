N = int(input())
cities = list(map(int, input().split()))
M = int(input())

min_m = 0
max_m = max(cities)

while min_m <= max_m:
    mid_m = (min_m + max_m) // 2

    total_m = 0

    for city in cities:
        total_m += min(mid_m, city)

        if total_m > M:
            max_m = mid_m - 1
            break

    else:
        min_m = mid_m + 1

print(max_m)
