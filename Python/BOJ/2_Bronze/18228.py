N = int(input())
ice = list(map(int, input().split()))
temp = 1000000000
result = 0
for i in ice:
    if i == -1:
        result += temp
        temp = 1000000000
        continue

    temp = min(i, temp)

result += temp
print(result)
