def solution(s):
    answer = []

    for word in s:
        word_stack = []
        cnt110 = 0

        # 문자열에서 110의 개수 추출 및 110외 문자열 계산
        for w in word:
            if len(word_stack) > 1 and w == '0' and word_stack[-1] == '1' and word_stack[-2] == '1':
                word_stack.pop()
                word_stack.pop()

                cnt110 += 1
                continue

            word_stack.append(w)

        # 마지막으로 나오는 0 검색
        split_idx = 0
        for idx in range(len(word_stack)-1, -1, -1):
            if word_stack[idx] == '0':
                split_idx = idx + 1
                break

        # 마지막 0을 기준으로 나누고 110을 cnt만큼 삽입
        result = ''.join(word_stack[:split_idx]) + \
            '110'*cnt110 + ''.join(word_stack[split_idx:])
        answer.append(result)

    return answer
