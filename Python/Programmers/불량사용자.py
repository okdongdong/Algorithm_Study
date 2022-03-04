def comb(N, now, temp=set()):
    global result
    if now == N:
        result.append(''.join(sorted(list(temp))))
        return
    for i in banned_id_candidate_list[now]:
        if i in temp:
            continue
        temp.add(i)
        comb(N, now+1, temp)
        temp.remove(i)


def solution(user_id, banned_id):
    global result, banned_id_candidate_list
    result = []
    banned_id_candidate_list = [[] for _ in range(len(banned_id))]
    for i in range(len(user_id)):
        for j in range(len(banned_id)):
            if len(user_id[i]) != len(banned_id[j]):
                continue
            for k in range(len(user_id[i])):
                if banned_id[j][k] == '*':
                    continue
                if banned_id[j][k] != user_id[i][k]:
                    break
            else:
                banned_id_candidate_list[j].append(user_id[i])   # 불량사용자 후보

    comb(len(banned_id), 0)

    return len(set(result))


print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
