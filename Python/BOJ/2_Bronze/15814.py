txt = input()
T = int(input())
idx = list(range(len(txt)))
for _ in range(T):
    A, B = map(int, input().split())
    idx[A], idx[B] = idx[B], idx[A]

result = ''
for i in idx:
    result += txt[i]

print(result)