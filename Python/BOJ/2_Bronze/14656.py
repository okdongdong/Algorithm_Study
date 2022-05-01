input()
num = list(map(int, input().split()))
cnt = 0
for idx, val in enumerate(num):
    if idx+1 != val:
        cnt += 1
print(cnt)
