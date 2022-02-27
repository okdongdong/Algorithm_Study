# 기준 건물과 가까운 건물간의 기울기보다 작은 경우 안보임
# 한 쪽에서 보이면 다른 쪽도 보임
# import numpy as np                    # 백준에서 런타임에러 발생

N = int(input())
BH = [int(b) for b in input().split()]  # BH : building_height
table = [[0 for _ in range(N)] for _ in range(N)]

for BB in range(N - 1):                 # BB : base_building
    MG = -1000000001                    # MG : max_gradient
        
    for CB in range(BB + 1, N):         # CB : compare_building
        gradient = (BH[CB] - BH[BB]) / (CB - BB)
            
        if gradient > MG:
            MG = gradient
            table[BB][CB] = table[CB][BB] = 1

building_lst = []
for i in range(N):
    building_lst.append(sum(table[i]))  # 각 건물에서 보이는 건물 수 계산

print(max(building_lst))


