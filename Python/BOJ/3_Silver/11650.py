# 좌표 정렬하기
import sys
input = sys.stdin.readline
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort()
for i in range(N):
    print(*xy[i])


