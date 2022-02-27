# 노래 악보
N, Q = map(int, input().split())
sheet = [int(input()) for _ in range(N)]
questions = [int(input()) for _ in range(Q)]
arr = []

for idx, val in enumerate(sheet):
    arr += [idx+1] * val

result = []
for q in questions:
    result.append(arr[q])

print(*result, sep='\n')
