import sys

def find_me():                              # 현재 나의 위치를 찾아줄 함수
    for x in range(N):
        for y in range(M):
            if campus[x][y] == 'I':
                return (x, y)               # 현재 좌표 반환


N, M = map(int, input().split())
campus = [input() for _ in range(N)]
# campus = sys.stdin.read().splitlines()

move = [(-1, 0), (0, -1), (1, 0), (0, 1)]   # 이동 가능한 경우의 수

stack = [find_me()]                         # 나의 위치를 찾아 스택에 넣어줌
flag = [[True]*M for _ in range(N)]         # 방문한 위치를 체크하기 위한 리스트
cnt = 0                                     # P 개수 카운트

while stack:

    dx, dy = stack.pop()                    # 이동할 좌표를 stack에서 하나씩 가져옴
    for xy in move:                         # 상하좌우에 대해 확인
        x = dx + xy[0]
        y = dy + xy[1]
   
        if (0 <= x < N) and (0 <= y < M):   # 좌표가 캠퍼스 범위내에 있는지 체크
            if (campus[x][y] != 'X') and flag[x][y]:
                stack.append((x, y))
                flag[x][y] = False          # 한번 방문한 곳은 재방문 하지 않음
               
                if campus[x][y] == 'P':
                    cnt += 1

if cnt:
    print(cnt)
else:
    print('TT')
