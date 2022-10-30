S = input()

left = []
right = []

for i in range(len(S) - 1, -1, -1):
    for j in range(i):
        if S[i] > S[j]:
            right.append(S[i])
            break

    else:
        left.append(S[i])

result = "".join(left + right[::-1])

print(result)
