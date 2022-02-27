# 1865. 동철이의 일 분배

def task(man=0, prob=100):
    global max_prob
    if prob <= max_prob:
        return

    if man == N:
        max_prob = prob
        return

    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        task(man+1, prob*probs[man][i]/100)
        check[i] = False


T = int(input())
result = []
for tc in range(1, T+1):
    N = int(input())
    probs = [list(map(int, input().split())) for _ in range(N)]
    check = [False]*N
    max_prob = 0
    task()
    result.append(f'#{tc} {max_prob:0.06f}')

print('\n'.join(result))