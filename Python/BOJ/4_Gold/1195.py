a = input()
b = input()
a, b = sorted((a, b), key=lambda x: len(x))

min_w = len(a) + len(b)
c = "0" * (len(a)) + b + "0" * (len(a))

for i in range(len(c) - len(a)):
    for j in range(len(a)):
        if a[j] == "2" and c[i + j] == "2":
            break
    else:
        min_w = min(
            min_w,
            (len(a) + len(b) - i if i < len(a) else len(b) if i <= len(b) else i),
        )

print(min_w)
