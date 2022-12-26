txt = input()
key = input()
key = key * ((len(txt) // len(key)) + 1)
result = ""

for i in range(len(txt)):
    if txt[i] == " ":
        result += " "
        continue

    result += chr((ord(txt[i]) - ord(key[i]) - 1) % 26 + 97)

print(result)
