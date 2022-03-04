N, new_score, P = map(int, input().split())

if N:
    ranking_list = list(map(int, input().split()))
    ranking = 1
    result = 1
    for score in ranking_list:
        if score > new_score:
            result += 1
            ranking += 1
        elif score == new_score:
            ranking += 1
        else:
            break
    if ranking > P:
        result = -1

else:
    result = 1

print(result)
