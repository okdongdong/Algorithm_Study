# 농구 경기
N = int(input())
names = dict()
for _ in range(N):
    temp = input()
    f = temp[0]
    if names.get(f):
        names[f] += 1
    else:
        names[f] = 1

result = []
for name, cnt in names.items():
    if cnt >= 5:
        result.append(name)

if result:
    result.sort()
    print(''.join(result))
else:
    print('PREDAJA')