# 오르막수

N = int(input())

lst = [1]*10
pre_lst = list(range(0,11))

for _ in range(N-1):
    for i in range(1, 10):
        lst[i] = (lst[i-1] + pre_lst[i])%10007
        pre_lst = lst

print(sum(lst)%10007)