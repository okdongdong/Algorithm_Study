def solution(gems):
    gem_num = len(set(gems))
    gem_dict = dict()
    min_range_cnt = len(gems)
    min_range = [1, len(gems)]
    left, right = 0, -1
    while left < len(gems) - 1 or right < len(gems)-1:
        temp_cnt = len(gem_dict)

        if temp_cnt < gem_num and right < len(gems)-1:
            right += 1
            if gem_dict.get(gems[right]):
                gem_dict[gems[right]] += 1
            else:
                gem_dict[gems[right]] = 1

        else:
            if min_range_cnt > right-left+1 and temp_cnt == gem_num:
                min_range_cnt = right-left+1
                min_range = [left+1, right+1]
            if gem_dict[gems[left]] == 1:
                del gem_dict[gems[left]]  # 개수가 0인 보석은 딕셔너리에서 삭제해서 시간을 줄여줌
            else:
                gem_dict[gems[left]] -= 1
            left += 1

    return min_range


print(solution(["DIA", "RUBY", "RUBY", "DIA",
      "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]	))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["A", "A", "A", "B", "B"]))
print(solution(["A"]))
print(solution(["A", "B", "B", "B", "B", "B", "B", "C", "B", "A"]))
