# 주사위 윷놀이

# 말 4개
# 파란칸: 파란 화살표, 다른칸: 빨간 화살표
# 10턴, 1~5주사위, 말을 골라 이동
# 말이 도착하는 칸에 말이 있으면 안됨
# 최대점수
# 브루트포스 => 4**10 == 1048576

def move(score=0, dice_idx=0):
    global max_score
    if dice_idx == 10:
        if max_score < score:
            max_score = score
        return

    for i in range(4):
        temp_horse = horse[i][:]
        now, track_num = horse[i]
        if track_list[track_num][now] > 40:
            continue

        if track_num == 0 and (track_list[track_num][now] in blue_area):
            track_num = track_list[track_num][now]//10
            now = 0
        
        now += dice_list[dice_idx]
        horse[i] = [now, track_num]

        for h in range(4):  # 이미 말이 있는 위치로 이동하려고 하는 경우
            other_now, other_track_num = horse[h]
            if i == h:
                continue
            if horse[i] == horse[h] and track_list[track_num][now] <= 40: # 0번트랙인 경우
                break
            if track_num and other_track_num and track_list[track_num][now] < 40 and track_list[track_num][now] == track_list[other_track_num][other_now]:
                break
            if track_list[track_num][now] == track_list[other_track_num][other_now] == 40:  # 40에서 만나는 경우
                break
        else:
            if track_list[track_num][now] > 40: # 말이 도착하는 경우
                move(score, dice_idx+1)
            else:   
                move(score+track_list[track_num][now], dice_idx+1)

        horse[i] = temp_horse


dice_list = list(map(int, input().split()))
horse = [[0, 0] for _ in range(4)]  # 현재위치, track_num
max_score = 0
# 파란화살표
blue_area = set([10, 20, 30])
track_list = [
    list(range(0, 60, 2)),
    [10, 13, 16, 19, 25, 30, 35, 40, 9999, 9999, 9999, 9999, 9999],
    [20, 22, 24, 25, 30, 35, 40, 9999, 9999, 9999, 9999, 9999],
    [30, 28, 27, 26, 25, 30, 35, 40, 9999, 9999, 9999, 9999, 9999],
]   # 인덱스에러 방지위해 리스트 뒤에 더 추가해줌

move()
print(max_score)
