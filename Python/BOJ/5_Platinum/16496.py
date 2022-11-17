input()
a = "".join(sorted(input().split(), key=lambda x: x * 10, reverse=True))
print(0 if a[0] == "0" else a)
