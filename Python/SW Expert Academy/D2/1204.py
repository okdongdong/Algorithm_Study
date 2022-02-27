T = int(input())
for _ in range(T):
    N = int(input())
    scores = [int(i) for i in input().split()]
    score_dict = {}
    max_cnt = 0
    mode_score = 0
    for score in scores:
        try:
            score_dict[score] += 1
        except:
            score_dict[score] = 1

    for score, cnt in score_dict.items():
        if cnt > max_cnt:
            max_cnt = cnt
            mode_score = score
        
        elif cnt == max_cnt and score > mode_score:
            mode_score = score
    
    print(f'#{N} {mode_score}')