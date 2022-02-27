N = int(input())
num_lst = []
cnt = 0
for num in range(1, N+1):
    if num < 100:
        cnt += 1
    elif num < 1000:
        a, b, c = map(int, [n for n in str(num)])
        if a - b == b - c:
            cnt += 1
print(cnt)