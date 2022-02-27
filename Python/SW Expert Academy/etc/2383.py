# 2383. [모의 SW 역량테스트] 점심 식사시간

def cal_time():
    distance = [[0, 0, 0] for _ in range(len(people))]      # stair_num, distance, stair_distance
    for i in range(len(people)):
        pr, pc = people[i]
        sd, sr, sc = stairs[check[i]]
        distance[i] = [check[i], abs(pr-sr) + abs(pc-sc), sd]

    move_time = 0
    stair_person = [set(),set()]
    
    while True:
        move_time += 1
        for i in range(len(distance)):
            if distance[i][1] > 0:
                distance[i][1] -=1
                continue

            if distance[i][2] > 0 and len(stair_person[distance[i][0]]) < 3:
                stair_person[distance[i][0]].add(i)

            if i in  stair_person[distance[i][0]]:
                distance[i][2] -= 1
            
            if distance[i][2] <= 0:
                stair_person[distance[i][0]].remove(i)
            





T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stairs = []
    people = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                people.append((r, c))

            elif arr[r][c] > 1:
                stairs.append((arr[r][c], r, c))

    check = [0]*len(people)
    for i in range(1 << len(people)):
        for j in range(len(people)):
            if i & (1 << j):
                check[j] = 1
            else:
                check[j] = 0
        cal_time()
