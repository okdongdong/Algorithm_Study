N = int(input())
cranes = sorted(map(int, input().split()), reverse=True)

M = int(input())
boxes = sorted(map(int, input().split()))

result = -1

for t in range(1, M + 1):
    temp = []
    i = 0
    while i < N and boxes:
        box = boxes.pop()
        if box > cranes[i]:
            temp.append(box)

        else:
            i += 1

    boxes = boxes + temp[::-1]
    if not boxes:
        result = t
        break

print(result)
