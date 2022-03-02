import sys

txt = sys.stdin.read() 

alpha = [0]*26
for t in txt:
    if t.islower():
        alpha[ord(t)-97] += 1

for i in range(26):
    if max(alpha) == alpha[i]:
        print(chr(i+97), end='')
