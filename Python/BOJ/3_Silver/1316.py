n=int(input())
cnt = 0

for _ in range(n):
    word = input()
    boo = True
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if word[i] in new_word:
                boo = False
                break
    if boo == True:
        cnt += 1

print(cnt)
