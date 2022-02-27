# 8진수, 10진수, 16진수
num = input()
if num[0] == '0':
    if num[1] == 'x':
        num = int(num[2:], 16)
    else:
        num = int(num[1:], 8)
print(num)
