# 분해합
def cal_num(num):
    num_sum = 0
    temp = num
    while temp:
        temp, n = divmod(temp, 10)
        num_sum += n
    if num + num_sum == N:
        return num
    return 0

N = int(input())
result = 0
if N < 100:
    for num in range(N):
        result = cal_num(num)
        if result:
            break

else:
    for num in range(N-100, N):
        result = cal_num(num)
        if result:
            break

print(result)