# 요세푸스 문제 0
N, K = map(int, input().split())
check = [False]*N
cnt = 0
result = []
idx = -1
while len(result) < N:
    idx += 1
    if idx == N:
        idx = 0

    if check[idx]:
        continue

    cnt += 1

    if cnt == K:
        result.append(str(idx+1))
        check[idx] = True
        cnt = 0

print(f"<{', '.join(result)}>")
