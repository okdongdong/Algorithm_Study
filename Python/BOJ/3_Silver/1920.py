# 수 찾기

N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
result = []
for m in M_list:
    if m in N_list:
        result.append(1)
    else:
        result.append(0)
print(*result, sep='\n')

