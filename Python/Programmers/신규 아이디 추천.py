def solution(new_id):
    # step 1
    new_id = new_id.lower()

    # step 2 & 3
    usable_txt = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', '0', '-', '_', '.'
    }

    temp_id = []
    for txt in new_id:
        if txt in usable_txt:
            if txt == '.' and (not temp_id or (temp_id and temp_id[-1] == '.')):
                continue

            temp_id.append(txt)

    # step 5 & 7
    if not temp_id:
        return 'aaa'

    # step 4
    if temp_id[-1] == '.':
        temp_id.pop()

    # step 6
    if len(temp_id) >= 15:
        temp_id = temp_id[:15]

    if temp_id[-1] == '.':
        temp_id.pop()

    while len(temp_id) <= 2:
        temp_id.append(temp_id[-1])

    return ''.join(temp_id)


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
