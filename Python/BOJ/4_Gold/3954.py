# Brainf**k 인터프리터

T = int(input())
result_list = []
for _ in range(T):
    S_m, S_c, S_i = map(int, input().split())
    cmd_list = input()
    txt = list(map(ord, list(input())))
    txt_idx = 0
    arr = [0] * S_m
    cmd_dict = dict()

    # 괄호를 서로 짝지어줌
    stack = []
    for idx in range(S_c):
        cmd = cmd_list[idx]
        if cmd == '[':
            stack.append(idx)
        if cmd == ']':
            left_idx = stack.pop()
            cmd_dict[idx] = left_idx
            cmd_dict[left_idx] = idx

    cnt = 0
    idx = 0
    loop_idx = 0
    pointer = 0
    result = 'Terminates'

    while cnt < 50000000:
        if idx >= S_c:
            break

        cmd = cmd_list[idx]

        if cmd == '-':
            arr[pointer] -= 1
            arr[pointer] %= 256

        elif cmd == '+':
            arr[pointer] += 1
            arr[pointer] %= 256

        elif cmd == '<':
            pointer -= 1
            pointer %= S_m

        elif cmd == '>':
            pointer += 1
            pointer %= S_m

        elif cmd == '[':
            if arr[pointer] == 0:
                idx = cmd_dict[idx]

        elif cmd == ']':
            if arr[pointer] != 0:
                idx = cmd_dict[idx]

        elif cmd == '.':
            pass

        elif cmd == ',':
            if txt_idx >= S_i:
                arr[pointer] = 255
            else:
                arr[pointer] = txt[txt_idx]
                txt_idx += 1

        cnt += 1
        idx += 1

    else:
        for _ in range(50000000):
            if idx >= S_c:
                break

            cmd = cmd_list[idx]

            if cmd == '-':
                arr[pointer] -= 1
                arr[pointer] %= 256

            elif cmd == '+':
                arr[pointer] += 1
                arr[pointer] %= 256

            elif cmd == '<':
                pointer -= 1
                pointer %= S_m

            elif cmd == '>':
                pointer += 1
                pointer %= S_m

            elif cmd == '[':
                if arr[pointer] == 0:
                    idx = cmd_dict[idx]

            elif cmd == ']':
                if arr[pointer] != 0:
                    loop_idx = max(loop_idx, idx)
                    idx = cmd_dict[idx]

            elif cmd == '.':
                pass

            elif cmd == ',':
                if txt_idx >= S_i:
                    arr[pointer] = 255
                else:
                    arr[pointer] = txt[txt_idx]
                    txt_idx += 1

            idx += 1
        else:
            result = 'Loops {} {}'.format(cmd_dict[loop_idx], loop_idx)

    result_list.append(result)
print(*result_list, sep='\n')
