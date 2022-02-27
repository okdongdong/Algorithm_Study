N = int(input())
dir_list = [input() for _ in range(N)]
txt = dir_list.pop()
result = ''

for i in range(len(txt)):
    for dir in dir_list:
        if txt[i] != dir[i] and txt[i] != '?':
            result += '?'
            break

    else:
        result += txt[i]

print(result)
