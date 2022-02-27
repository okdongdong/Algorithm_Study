# 미네랄
# 순서 : 왼 오 왼 오 ...
# 높이 1 : 바닥
# 높이 R : 천장

import sys
input = sys.stdin.readline


def find_mineral(visited):
    for r in range(R):
        for c in range(C):
            if cave[r][c] == 'x' and not visited[r][c]:
                return (r, c)
    return False


def check_cluster(r, c):
    visited = [[False]*C for _ in range(R)]
    stack = [find_mineral(visited)]
    while stack:
        r, c = stack.pop()
        visited[r][c] = True
        for dr, dc in drc:
            nr, nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and cave[nr][nc]=='x' and not visited[nr][nc]:
                stack.append((nr, nc))

    if find_mineral(visited): # 클러스터가 분할되는 경우
        gravity()


def gravity(r, c):
    pass


R, C = map(int, input().split())
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cave = [list(input().split()) for _ in range(R)]

N = int(input())
sticks = list(map(int, input().split()))

is_left = True  # 왼쪽사람인지 오른쪽사람인지 판단

for stick in sticks:
    is_broken = False   # 미네랄을 파괴했는지 확인
    r = R - sticks
    if is_left:
        for c in range(C):
            if cave[r][c] == 'x':
                if is_broken:   # 미네랄이 파괴된 후 클러스터가 분할되는 지 확인
                    
                    break       # 클러스터 분할되지 않은 경우

                else:   # 미네랄 파괴
                    is_broken = True
                    cave[r][c] = '.'

        else:   # 미네랄을 파괴한 후 클러스터가 분할되는 경우

    else:
        for c in range(C-1, -1, -1):
