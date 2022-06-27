# 문자열
a, b = input().split()

if len(a) < len(b):
    a, b = b, a

min_cnt = 987654321

for w in range(len(a) - len(b) + 1):
    cnt = 0
    for i in range(len(b)):
        if a[i+w] != b[i]:
            cnt += 1
    min_cnt = min(min_cnt, cnt)

print(min_cnt)
