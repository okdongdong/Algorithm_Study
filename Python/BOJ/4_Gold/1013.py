# Contact
import sys
input = sys.stdin.readline

N = int(input())
result_list = []

for _ in range(N):
    signal = input().rstrip()
    zero_cnt = 0
    flag1 = False
    flag2 = False
    flag3 = False
    result = 'NO'
    if signal[-1] == '1':
        for s in signal:
            if flag1 and flag2:
                if s == '1':
                    flag3 = True
                    continue

                if flag3:
                    flag2 = False

                else:
                    flag1 = False
                    flag2 = False

            if flag2:
                if s == '1':
                    flag2 = False
                    continue

                break

            if flag1:
                if s == '1':
                    if flag3 and zero_cnt == 1:
                        flag1 = False
                        flag3 = False
                        zero_cnt = 0
                        continue

                    if zero_cnt < 2:
                        break

                    flag2 = True
                    flag3 = False
                    zero_cnt = 0
                    continue

                if s == '0':
                    zero_cnt += 1
                    continue

            if s == '1':
                flag1 = True

            else:
                flag2 = True

        else:
            if (not flag1 or flag2):
                result = 'YES'

    result_list.append(result)

print('\n'.join(result_list))
