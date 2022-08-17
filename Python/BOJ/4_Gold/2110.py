N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

houses.sort()
max_dist = houses[-1] - houses[0]


left, right = 1, 1000000000
while left <= right:
    mid = (right + left)//2
    cnt = 1
    if max_dist < right:
        right = mid
        continue

    i, j = 0, 1

    while j < N:
        dist = houses[j] - houses[i]

        if dist >= mid:
            cnt += 1
            i = j

        j += 1

        if cnt >= C:
            left = mid + 1
            break

    else:
        right = mid - 1

print(right)
