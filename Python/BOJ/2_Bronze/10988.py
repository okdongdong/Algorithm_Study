txt = input()
result = 0

for i in range(len(txt)//2):
    if txt[i] != txt[-i-1]:
        break
else:
    result = 1

print(result)
