# Jogo de Estratégia
J, R = map(int, input().split())
rounds = list(map(int, input().split()))
scores = [0]*J
for i in range(J*R):
    scores[i % J] += rounds[i]
max_J = (scores[-1], rounds[-1], J)
for i in range(J):
    max_J = max(max_J, (scores[i], rounds[-J+i], i+1))
print(max_J[2])
