# 벡터 매칭
from itertools import combinations
  
T = int(input())
result = []
for _ in range(T):
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    start_points_list = list(combinations(range(N),N//2))
    min_sum = 987654321
    for start_points in start_points_list:
        x_sum = 0
        y_sum = 0
        for idx, point in enumerate(points):
            if idx in start_points:
                x_sum -= point[0]
                y_sum -= point[1]
            else:
                x_sum += point[0]
                y_sum += point[1]
        temp_sum = (x_sum**2 + y_sum**2)**0.5

        if temp_sum < min_sum:
            min_sum = temp_sum
    result.append(min_sum)

print(*result, sep='\n')


