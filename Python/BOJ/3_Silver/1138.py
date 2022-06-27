N = int(input())
nums = list(map(int, input().split()))

result = [0]*N

for idx, num in enumerate(nums):
    cnt = 0

    for i in range(N):
        if not result[i]:
            cnt += 1

        if cnt > num:
            result[i] = idx + 1
            break

print(*result)
