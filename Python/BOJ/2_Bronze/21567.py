a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)
num_cnt = [0]*10
for n in num:
    num_cnt[int(n)] += 1
print(*num_cnt, sep='\n')
