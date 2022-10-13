N = int(input())
nums = [int(input()) for _ in range(N)]
ranges = [range(N), range(N - 1, -1, -1)]

for r in ranges:
    now_max, cnt = 0, 0
    for i in r:
        if nums[i] > now_max:
            now_max = nums[i]
            cnt += 1
    print(cnt)
