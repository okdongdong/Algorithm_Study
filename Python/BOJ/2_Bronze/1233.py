a, b, c = map(int, input().split())
cnt = [0]*81
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            cnt[i+j+k] += 1
print(cnt.index(max(cnt)))
