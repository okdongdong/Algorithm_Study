# 게리맨더링 2

def cal(x, y, d1, d2):
    district = [[0]*N for _ in range(N)]
    people_cnt = [0]*6
    for r in range(N):
        for c in range(N):
            if 0 <= r < x+d1 and 0 <= c <= y:
                district[r][c] = 1
            elif 0 <= r <= x+d2 and y < c < N:
                district[r][c] = 2
            elif x+d1 <= r < N and 0 <= c < y-d1+d2:
                district[r][c] = 3
            elif x+d2 < r < N and y-d1+d2 <= c < N:
                district[r][c] = 4

    for i in range(d1+1):
        district[x+i][y-i] = 5
        district[x+d2+i][y+d2-i] = 5

    for i in range(d2+1):
        district[x+i][y+i] = 5
        district[x+d1+i][y-d1+i] = 5

    for r in range(x+1,x+d1+d2):
        flag = False
        for c in range(y-d1, y+d2+1):
            if district[r][c] == 5 and flag:
                break
            
            if flag:
                district[r][c] = 5

            if district[r][c] == 5:
                flag = True


    for r in range(N):
        for c in range(N):
            people_cnt[district[r][c]] += people[r][c]
    people_cnt.pop(0)
    return max(people_cnt)-min(people_cnt)


N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
min_people_diff = 40001
for x in range(N):
    for y in range(N):
        for d1 in range(N):
            for d2 in range(N):
                if 0<= x < x+d1+d2 < N and 0 <= y-d1 < y < y+d2 < N:
                    people_diff = cal(x,y,d1,d2)
                    if people_diff < min_people_diff:
                        min_people_diff = people_diff

print(min_people_diff)
