N, K = input().split()
K = int(K)

if len(N) == 1 or (len(N) == 2 and N[-1] == '0'):
    result = -1

else:
    num = list(N)
    max_num = sorted(num, reverse=True)

    idx = 0
    while max_num != num and K > 0 and idx < len(num):
        max_val = num[idx]
        max_idx_list = []
        for i in range(idx+1, len(N)):
            if max_val < num[i]:
                max_val = num[i]
                max_idx_list = [i]
            elif max_val == num[i]:
                max_idx_list.append(i)

        idx_add = 0
        while idx+idx_add+1 < len(num) and num[idx+idx_add] == max_val:
            idx_add += 1

        sub_num = num[idx+idx_add:idx+min(len(max_idx_list), K)]
        sub_num.sort()
        sub_idx = 0
        max_idx = len(max_idx_list)-1

        while sub_idx < len(sub_num) and K > 0 and idx < len(num) and sub_num[sub_idx] < max_val:
            if num[idx] == max_val:
                idx += 1
                continue

            num[max_idx_list[max_idx]], num[idx] = sub_num[sub_idx], max_val

            idx += 1
            max_idx -= 1
            sub_idx += 1
            K -= 1

        if not sub_num:
            idx += 1

        K += len(sub_num) - 1 if len(sub_num) - 1 > 0 else 0

    if K % 2 and len(set(num)) == len(num):
        num[-1], num[-2] = num[-2], num[-1]

    result = ''.join(num)

print(result)
