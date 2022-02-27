alpha = input()
lst = []
for a in alpha:
    num = ord(a) - 64
    lst.append(str(num))

print(' '.join(lst))