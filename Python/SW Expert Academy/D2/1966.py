## bubble sort

T = int(input())

for tc in range(T):
    N = int(input())
    nums = [int(i) for i in input().split()]

    for n in range(N - 1, 0, -1):
        for i in range(n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    print('#{}'.format(tc + 1), end=' ')
    print(*nums)


## counting sort

def mymax(lst):
    max_number = lst[0]
    for i in lst:
        if i > max_number:
            max_number = i
    return max_number


T = int(input())

for tc in range(T):
    N = int(input())
    nums = [int(i) for i in input().split()]
    max_num = mymax(nums)+1
    num_cnts = [0] * max_num
    results = [0] * N

    for num in nums:
        num_cnts[num] += 1

    for i in range(1,max_num):
        num_cnts[i] += num_cnts[i-1]

    for num in nums:
        num_cnts[num] -= 1
        results[num_cnts[num]] = num

    print('#{}'.format(tc + 1), end=' ')
    print(*results)




