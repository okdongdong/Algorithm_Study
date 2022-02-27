N, M = map(int, input().split())
num_lst = [int(i) for i in input().split()]

max_num = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            num = num_lst[i] + num_lst[j] + num_lst[k]
            
            if max_num < num <= M:
                max_num = num

print(max_num)
