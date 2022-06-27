dishes = input()
result = 10

for i in range(1, len(dishes)):
    if dishes[i] == dishes[i-1]:
        result += 5

    else:
        result += 10

print(result)
