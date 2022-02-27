# 인생 점수
N = int(input())
result = []
for _ in range(N):
    text = input()
    score = 0
    for t in text:
        if t != ' ':
            score += ord(t)-64

    if score == 100:
        result.append('PERFECT LIFE')
    else:
        result.append(str(score))

print('\n'.join(result))
