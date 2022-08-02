# 진짜 공간
from math import ceil


N = int(input())
files = list(map(int, input().split()))
cluster = int(input())

cnt = 0

for file in files:
    cnt += ceil(file/cluster)

print(cnt * cluster)
