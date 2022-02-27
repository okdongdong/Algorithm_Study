T = int(input())
for tc in range(1,T+1):
    nums = [int(i) for i in input().split()]
    max_num = nums[0]
    min_num = nums[0]
    sum_nums = 0
    cnt_nums = 0

    for num in nums:
        sum_nums += num
        cnt_nums += 1

        if max_num < num:
            max_num = num
    
        elif min_num > num:
            min_num = num

    result = (sum_nums - max_num - min_num)/(cnt_nums - 2)

    print('#{} {:0.0f}'.format(tc, result))
