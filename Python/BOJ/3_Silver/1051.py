def square():
    
    a = min(N, M)   
    for i in range(a,0,-1):

        for x in range(N):
            if x+i > N: 
                break
            for y in range(M):
                if y+i > M:
                    break

                if rectangle[x][y] == rectangle[x+i-1][y] == rectangle[x][y+i-1] == rectangle[x+i-1][y+i-1]:
                    # 정사각형의 네 좌표가 모두 같으면 넓이 반환
                    return i**2


N, M = map(int, input().split())
rectangle = [input() for _ in range(N)]

print(square())
