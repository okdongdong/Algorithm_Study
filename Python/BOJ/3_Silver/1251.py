txt = input()
N = len(txt)
result = []

for i in range(1, N - 1):
    for j in range(i + 1, N):
        a, b, c = txt[:i][::-1], txt[i:j][::-1], txt[j:][::-1]
        temp = a + b + c
        result.append(temp)

print(sorted(result)[0])
