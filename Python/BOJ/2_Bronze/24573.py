N = int(input())
cnt = 0
while N >= 0:
    if not N % 5:
        cnt += 1

    N -= 4

print(cnt)
