# 타임머신
# 벨만-포드 알고리즘
# 다익스트라에 비해 느리지만, 음수인 가중치가 있어도 계산가능

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s_e_t_list = [list(map(int, input().split())) for _ in range(M)]
city = [[0, 0] + [987654321]*(N-1) for _ in range(N+1)]
buses = [[] for _ in range(N+1)]

for s, e, t in s_e_t_list:
    buses[e].append((s, t))  # 도착 노드에 출발 노드 번호와 시간을 기록

for i in range(1, N+1):     # (N-1)번 반복 + 음의 사이클 발생확인 위해 +1번 반복
    for e in range(1, N+1): 
        for s, t in buses[e]:
            if city[i-1][s] == 987654321:   # s 노드가 기존에 도달가능한 노드였는지 확인
                continue
            city[i][e] = min(city[i][e], city[i-1][s] + t)

if city[-1] == city[-2]:    # 음의 사이클이 존재하지 않는경우
    result = []
    for i in range(2, N+1):
        result.append(str(city[-1][i] if city[-1][i] < 987654321 else -1))

else:
    result = ['-1']

print('\n'.join(result))
