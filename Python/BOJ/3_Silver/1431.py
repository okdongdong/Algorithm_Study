N = int(input())
serial_num = [input() for _ in range(N)]

serial_num_length = [len(num) for num in serial_num]
sum_lst = []
result_lst = []

for i in range(len(serial_num)):
    sum_num = 0
    for txt in serial_num[i]:
        try:
            sum_num += int(txt)
        except:
            pass
    sum_lst.append(sum_num)

new_lst = list(zip(serial_num, serial_num_length, sum_lst))
sorted_new_lst = sorted(new_lst, key=lambda x:(x[1], x[2], x[0])) # 정렬 다중조건 지정

for lst in sorted_new_lst:
    result_lst.append(lst[0])

print(*result_lst, sep='\n')