N = int(input())
name = input()
score = 0
for n in name:
    score += ord(n) - 64

print(score)