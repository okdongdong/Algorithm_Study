# 5215. 햄버거 다이어트

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    buger = [list(map(int, input().split())) for _ in range(N)]
    max_happy = 0
    for i in range(1<<N):
        cal, happy = 0, 0
        for j in range(N):
            if i & (1<<j):
                happy += buger[j][0]
                cal += buger[j][1]
        if cal <= L:
            if max_happy < happy:
                max_happy = happy

    print('#{} {}'.format(tc, max_happy))