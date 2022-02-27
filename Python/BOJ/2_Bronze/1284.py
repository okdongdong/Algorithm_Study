# 집 주소
import sys
input = sys.stdin.readline
result = []
while True:
    number = input().rstrip()

    if number == '0':
        break

    temp = 1
    for num in number:
        temp += 1
        if num == '0':
            temp += 4
        elif num == '1':
            temp += 2
        else:
            temp += 3
    result.append(str(temp))

print('\n'.join(result))